# Known issues

**Framework**: Swift Testing

Mark issues as known when running tests.

#### Overview

The testing library provides several functions named `withKnownIssue()` that you can use to mark issues as known. Use them to inform the testing library that a test should not be marked as failing if only known issues are recorded.

##### Mark an Expectation Failure As Known

Consider a test function with a single expectation:

```swift
@Test func grillHeating() throws {
  var foodTruck = FoodTruck()
  try foodTruck.startGrill()
  #expect(foodTruck.grill.isHeating) // ❌ Expectation failed
}
```

If the value of the `isHeating` property is `false`, `#expect` will record an issue. If you cannot fix the underlying problem, you can surround the failing code in a closure passed to `withKnownIssue()`:

```swift
@Test func grillHeating() throws {
  var foodTruck = FoodTruck()
  try foodTruck.startGrill()
  withKnownIssue("Propane tank is empty") {
    #expect(foodTruck.grill.isHeating) // Known issue
  }
}
```

The issue recorded by `#expect` will then be considered “known” and the test will not be marked as a failure. You may include an optional comment to explain the problem or provide context.

##### Mark a Thrown Error As Known

If an `Error` is caught by the closure passed to `withKnownIssue()`, the issue representing that caught error will be marked as known. Continuing the previous example, suppose the problem is that the `startGrill()` function is throwing an error. You can apply `withKnownIssue()` to this situation as well:

```swift
@Test func grillHeating() {
  var foodTruck = FoodTruck()
  withKnownIssue {
    try foodTruck.startGrill() // Known issue
    #expect(foodTruck.grill.isHeating)
  }
}
```

Because all errors thrown from the closure are caught and interpreted as known issues, the `withKnownIssue()` function is not throwing. Consequently, any subsequent code which depends on the throwing call having succeeded (such as the `#expect` after `startGrill()`) must be included in the closure to avoid additional issues.

> **Note**: `withKnownIssue()` is recommended instead of `#expect(throws:)` for any error which is considered a known issue so that the test status and results will reflect the situation more accurately.

##### Match a Specific Issue

By default, `withKnownIssue()` considers all issues recorded while invoking the body closure known. If multiple issues may be recorded, you can pass a trailing closure labeled `matching:` which will be called once for each recorded issue to determine whether it should be treated as known:

```swift
@Test func batteryLevel() throws {
  var foodTruck = FoodTruck()
  try withKnownIssue {
    let batteryLevel = try #require(foodTruck.batteryLevel) // Known
    #expect(batteryLevel >= 0.8) // Not considered known
  } matching: { issue in
    guard case .expectationFailed(let expectation) = issue.kind else {
      return false
    }
    return expectation.isRequired
  }
}
```

##### Resolve a Known Issue

If there are no issues recorded while calling `function`, `withKnownIssue()` will record a distinct issue about the lack of any issues having been recorded. This notifies you that the underlying problem may have been resolved so that you can investigate and consider removing `withKnownIssue()` if it’s no longer necessary.

##### Handle a Nondeterministic Failure

If `withKnownIssue()` sometimes succeeds but other times records an issue indicating there were no known issues, this may indicate a nondeterministic failure or a “flaky” test.

The first step in resolving a nondeterministic test failure is to analyze the code being tested and determine the source of the unpredictable behavior. If you discover a bug such as a race condition, the ideal resolution is to fix the underlying problem so that the code always behaves consistently even if it continues to exhibit the known issue.

If the underlying problem only occurs in certain circumstances, consider including a precondition. For example, if the grill only fails to heat when there’s no propane, you can pass a trailing closure labeled `when:` which determines whether issues recorded in the body closure should be considered known:

```swift
@Test func grillHeating() throws {
  var foodTruck = FoodTruck()
  try foodTruck.startGrill()
  withKnownIssue {
    // Only considered known when hasPropane == false
    #expect(foodTruck.grill.isHeating)
  } when: {
    !hasPropane
  }
}
```

If the underlying problem is unpredictable and fails at random, you can pass `isIntermittent: true` to let the testing library know that it will not always occur. Then, the testing library will not record an issue when zero known issues are recorded:

```swift
@Test func grillHeating() throws {
  var foodTruck = FoodTruck()
  try foodTruck.startGrill()
  withKnownIssue(isIntermittent: true) {
    #expect(foodTruck.grill.isHeating)
  }
}
```

## Topics

### Recording known issues in tests
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void)](withknownissue(_:isintermittent:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void) async](withknownissue(_:isintermittent:isolation:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void, when: () -> Bool, matching: KnownIssueMatcher) rethrows](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void, when: () async -> Bool, matching: KnownIssueMatcher) async rethrows](withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [typealias KnownIssueMatcher](knownissuematcher.md)
  A function that is used to match known issues.
### Describing a failure or warning
- [struct Issue](issue.md)
  A type describing a failure or warning which occurred during a test.

## See Also

- [Expectations and confirmations](expectations.md)
  Check for expected values, outcomes, and asynchronous events in tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/known-issues)*