# Enabling and disabling tests

**Framework**: Swift Testing

Conditionally enable or disable individual tests before they run.

#### Overview

Often, a test is only applicable in specific circumstances. For instance, you might want to write a test that only runs on devices with particular hardware capabilities, or performs locale-dependent operations. The testing library allows you to add traits to your tests that cause runners to automatically skip them if conditions like these are not met.

> **Note**: A condition may be evaluated multiple times during testing.

A condition may be evaluated multiple times during testing.

##### Disable a Test

If you need to disable a test unconditionally, use the [`disabled(_:sourceLocation:)`](trait/disabled(_:sourcelocation:).md) function. Given the following test function:

```swift
@Test("Food truck sells burritos")
func sellsBurritos() async throws { ... }
```

Add the trait  the test’s display name:

```swift
@Test("Food truck sells burritos", .disabled())
func sellsBurritos() async throws { ... }
```

The test will now always be skipped.

It’s also possible to add a comment to the trait to present in the output from the runner when it skips the test:

```swift
@Test("Food truck sells burritos", .disabled("We only sell Thai cuisine"))
func sellsBurritos() async throws { ... }
```

##### Enable or Disable a Test Conditionally

Sometimes, it makes sense to enable a test only when a certain condition is met. Consider the following test function:

```swift
@Test("Ice cream is cold")
func isCold() async throws { ... }
```

If it’s currently winter, then presumably ice cream won’t be available for sale and this test will fail. It therefore makes sense to only enable it if it’s currently summer. You can conditionally enable a test with [`enabled(if:_:sourceLocation:)`](trait/enabled(if:_:sourcelocation:).md):

```swift
@Test("Ice cream is cold", .enabled(if: Season.current == .summer))
func isCold() async throws { ... }
```

It’s also possible to conditionally  a test and to combine multiple conditions:

```swift
@Test(
  "Ice cream is cold",
  .enabled(if: Season.current == .summer),
  .disabled("We ran out of sprinkles")
)
func isCold() async throws { ... }
```

If a test is disabled because of a problem for which there is a corresponding bug report, you can use one of these functions to show the relationship between the test and the bug report:

- [`bug(_:_:)`](trait/bug(_:_:).md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-10yf5.md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-3vtpl.md)

For example, the following test cannot run due to bug number `"12345"`:

```swift
@Test(
  "Ice cream is cold",
  .enabled(if: Season.current == .summer),
  .disabled("We ran out of sprinkles"),
  .bug(id: "12345")
)
func isCold() async throws { ... }
```

If a test has multiple conditions applied to it, they must  pass for it to run. Otherwise, the test notes the first condition to fail as the reason the test is skipped.

##### Handle Complex Conditions

If a condition is complex, consider factoring it out into a helper function to improve readability:

```swift
func allIngredientsAvailable(for food: Food) -> Bool { ... }

@Test(
  "Can make sundaes",
  .enabled(if: Season.current == .summer),
  .enabled(if: allIngredientsAvailable(for: .sundae))
)
func makeSundae() async throws { ... }
```

## See Also

- [Limiting the running time of tests](limitingexecutiontime.md)
  Set limits on how long a test can run for until it fails.
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

*[View on Apple Developer](https://developer.apple.com/documentation/testing/enablinganddisabling)*