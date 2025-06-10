# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the provided ranges throughout the mutation closure, updating them to new ranges that represent the same effective locations after the mutation. If updating the provided ranges is not possible (tracking failed) then this function will fatal error. Use the Optional-returning variants to provide custom fallback behavior.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func transform<E>(updating ranges: inout [Range<AttributedString.Index>], body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `ranges`: A list of ranges to track throughout the   closure. The updated array (after the function is called) is guaranteed to be the same size as the provided array. Updated ranges are located at the same indices as their respective original ranges in the input   array.
- `body`: A mutating operation, or set of operations, to perform on the value of  . The value of   is provided to the closure as an   that the closure should mutate directly. Do not capture the value of   in the provided closure - the closure should mutate the provided   copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-3j625)*