# buildIf(_:)

**Framework**: Swift Charts  
**Kind**: method

Builds a partial result that’s conditionally present.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildIf<T>(_ content: T?) -> T? where T : ChartContent
```

#### Discussion

This method provides support for `if` statements. It produces optional chart content that is visible only when the condition evaluates to `true`.

## Parameters

- `content`: The content to use if the condition is  .

## See Also

- [static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2>](chartcontentbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.
- [static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2>](chartcontentbuilder/buildeither(second:).md)
  Builds a partial result from a condition that’s false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontentbuilder/buildif(_:))*