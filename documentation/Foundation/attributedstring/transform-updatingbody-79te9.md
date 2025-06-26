# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the provided range throughout the mutation closure, returning a new, updated range that represents the same effective locations after the mutation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func transform<E>(updating range: Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E) -> Range<AttributedString.Index>? where E : Error
```

#### Return Value

The updated `Range` that is valid after the mutation has been performed, or `nil` if the mutation performed does not allow for tracking to succeed (such as replacing the provided inout variable with an entirely different `AttributedString`).

## Parameters

- `range`: A range to track throughout the   block.
- `body`: A mutating operation, or set of operations, to perform on this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-79te9)*