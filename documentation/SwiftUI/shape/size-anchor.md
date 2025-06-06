# size(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func size(_ size: CGSize, anchor: UnitPoint) -> some Shape
```

#### Return Value

A new shape constrained to the given `size`, and positioned using `anchor`.

#### Discussion

The `anchor` parameter determines how the shape will be positioned within the container when the path’s bounds and the container’s bounds are not equal. This does not affect the layout properties of any views created from the shape (e.g. by filling it).

## Parameters

- `size`: The size to constrain the shape to.
- `anchor`: The anchor to use to determine how to position the new   shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/size(_:anchor:))*