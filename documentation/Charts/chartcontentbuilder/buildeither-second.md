# buildEither(second:)

**Framework**: Swift Charts  
**Kind**: method

Builds a partial result from a condition that’s false.

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
static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2> where T1 : ChartContent, T2 : ChartContent
```

#### Discussion

This method provides support for `if` statements with an `else` clause and `switch` statements. It produces optional chart content that is visible when the condition evaluates to `false`.

## Parameters

- `second`: The content to use if the condition is  .

## See Also

- [static func buildIf<T>(T?) -> T?](chartcontentbuilder/buildif(_:).md)
  Builds a partial result that’s conditionally present.
- [static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2>](chartcontentbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontentbuilder/buildeither(second:))*