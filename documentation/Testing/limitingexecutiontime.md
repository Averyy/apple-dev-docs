# Limiting the running time of tests

**Framework**: Swift Testing

Set limits on how long a test can run for until it fails.

#### Overview

Some tests may naturally run slowly: they may require significant system resources to complete, may rely on downloaded data from a server, or may otherwise be dependent on external factors.

If a test may hang indefinitely or may consume too many system resources to complete effectively, consider setting a time limit for it so that it’s marked as failing if it runs for an excessive amount of time. Use the [`timeLimit(_:)`](trait/timelimit(_:).md) trait as an upper bound:

```swift
@Test(.timeLimit(.minutes(60))
func serve100CustomersInOneHour() async {
  for _ in 0 ..< 100 {
    let customer = await Customer.next()
    await customer.order()
    ...
  }
}
```

If the above test function takes longer than an hour (60 x 60 seconds) to execute, the task in which it’s running is [`cancelled`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/task/cancel()) and the test fails with an issue of kind [`Issue.Kind.timeLimitExceeded(timeLimitComponents:)`](issue/kind-swift.enum/timelimitexceeded(timelimitcomponents:).md).

> **Note**: If multiple time limit traits apply to a test, the testing library uses the shortest time limit.

The testing library may adjust the specified time limit for performance reasons or to ensure tests have enough time to run. In particular, a granularity of (by default) one minute is applied to tests. The testing library can also be configured with a maximum time limit per test that overrides any applied time limit traits.

##### Apply Time Limits to Test Suites

When you apply a time limit to a test suite, the testing library recursively applies it to all test functions and child test suites within that suite. The time limit applies to each test in the test suite and any child test suites, or each test case for parameterized tests.

For example, if a suite contains five tests and you apply a time limit trait with a duration of one minute, then each test in the suite may run for up to one minute.

##### Apply Time Limits to Parameterized Tests

When you apply a time limit to a parameterized test function, the testing library applies it to each invocation  so that if only some cases cause failures due to timeouts, then the testing library doesn’t incorrectly mark successful cases as failing.

## See Also

- [Enabling and disabling tests](enablinganddisabling.md)
  Conditionally enable or disable individual tests before they run.
- [static func enabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](trait/enabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func enabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](trait/enabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func disabled(Comment?, sourceLocation: SourceLocation) -> Self](trait/disabled(_:sourcelocation:).md)
  Constructs a condition trait that disables a test unconditionally.
- [static func disabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](trait/disabled(if:_:sourcelocation:).md)
  Constructs a condition trait that disables a test if its value is true.
- [static func disabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](trait/disabled(_:sourcelocation:_:).md)
  Constructs a condition trait that disables a test if its value is true.
- [static func timeLimit(TimeLimitTrait.Duration) -> Self](trait/timelimit(_:).md)
  Construct a time limit trait that causes a test to time out if it runs for too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/limitingexecutiontime)*