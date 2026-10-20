# disabled(if:_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Type Method

Constructs a condition trait that disables a test if its value is true.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static func disabled(if condition: @autoclosure @escaping @Sendable () throws -> Bool, _ comment: Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation) -> Self
```

Available when `Self` is `ConditionTrait`.

#### Return Value

An instance of [`ConditionTrait`](../conditiontrait.md) that evaluates the closure you provide.

## Parameters

- `condition`: A closure that contains the trait’s custom condition logic. If this closure returns `false`, the trait allows the test to run. Otherwise, the testing library skips the test.
- `comment`: An optional comment that describes this trait.
- `sourceLocation`: The source location of the trait.

## See Also

### Customizing runtime behaviors
- [Enabling and disabling tests](../enablinganddisabling.md)
  Conditionally enable or disable individual tests before they run.
- [Limiting the running time of tests](../limitingexecutiontime.md)
  Set limits on how long a test can run for until it fails.
- [static func enabled(if: @autoclosure () throws -> Bool, Comment?, sourceLocation: SourceLocation) -> Self](./enabled%28if,_,sourcelocation%29.md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func enabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](./enabled%28_,sourcelocation,_%29.md)
  Constructs a condition trait that disables a test if it returns `false`.
- [static func disabled(Comment?, sourceLocation: SourceLocation) -> Self](./disabled%28_,sourcelocation%29.md)
  Constructs a condition trait that disables a test unconditionally.
- [static func disabled(Comment?, sourceLocation: SourceLocation, () async throws -> Bool) -> Self](./disabled%28_,sourcelocation,_%29.md)
  Constructs a condition trait that disables a test if its value is true.
- [static func timeLimit(TimeLimitTrait.Duration) -> Self](./timelimit%28_%29.md)
  Construct a time limit trait that causes a test to time out if it runs for too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/disabled(if:_:sourcelocation:))*