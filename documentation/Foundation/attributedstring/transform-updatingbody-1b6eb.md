# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the provided range throughout the mutation closure, updating the provided range to one that represents the same effective locations after the mutation.

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
mutating func transform<E>(updating range: inout Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

If updating the provided range is not possible (tracking failed) then this function will fatal error. Use the `Optional`-returning variants to provide custom fallback behavior.

## Parameters

- `range`: A range to track throughout the   closure.
- `body`: A mutating operation, or set of operations, to perform on the value of  . The value of   is provided to the closure as an   that the closure should mutate directly. Do not capture the value of   in the provided closure - the closure should mutate the provided   copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-1b6eb)*