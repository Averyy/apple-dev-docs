# disabled(_:sourceLocation:_:)

**Framework**: Swift Testing  
**Kind**: method

Constructs a condition trait that disables a test if its value is true.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static func disabled(_ comment: Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, _ condition: @escaping () async throws -> Bool) -> Self
```

#### Return Value

An instance of [`ConditionTrait`](conditiontrait.md) that evaluates the specified closure.

## Parameters

- `comment`: An optional comment that describes this trait.
- `sourceLocation`: The source location of the trait.
- `condition`: A closure that contains the trait’s custom condition logic.   If this closure returns  , the trait allows the test to run.   Otherwise, the testing library skips the test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait/disabled(_:sourcelocation:_:))*