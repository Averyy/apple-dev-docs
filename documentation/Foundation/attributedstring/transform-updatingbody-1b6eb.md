# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the provided range throughout the mutation closure, updating the provided range to one that represents the same effective locations after the mutation.

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
mutating func transform<E>(updating range: inout Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

If updating the provided range is not possible (tracking failed) then this function will fatal error. Use the `Optional`-returning variants to provide custom fallback behavior.

## Parameters

- `range`: A range to track throughout the   closure.
- `body`: A mutating operation, or set of operations, to perform on the value of  . The value of   is provided to the closure as an   that the closure should mutate directly. Do not capture the value of   in the provided closure - the closure should mutate the provided   copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-1b6eb)*