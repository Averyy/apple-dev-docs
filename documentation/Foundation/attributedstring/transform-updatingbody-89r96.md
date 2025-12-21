# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the provided ranges throughout the mutation closure, returning a new, updated range that represents the same effective locations after the mutation

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func transform<E>(updating ranges: [Range<AttributedString.Index>], body: (inout AttributedString) throws(E) -> Void) throws(E) -> [Range<AttributedString.Index>]? where E : Error
```

#### Return Value

The updated `Range`s that are valid after the mutation has been performed or `nil` if the mutation performed does not allow for tracking to succeed (such as replacing the provided inout variable with an entirely different `AttributedString`). When the return value is non-`nil`, the returned array is guaranteed to be the same size as the provided array with updated ranges at the same indices as their respective original ranges in the input array.

## Parameters

- `ranges`: Ranges to track throughout the   block.
- `body`: A mutating operation, or set of operations, to perform on this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-89r96)*