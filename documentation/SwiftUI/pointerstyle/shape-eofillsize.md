# shape(_:eoFill:size:)

**Framework**: SwiftUI  
**Kind**: method

Initializes a pointer style with a given shape.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func shape(_ shape: some Shape, eoFill: Bool = false, size: CGSize) -> PointerStyle
```

#### Discussion

For guidance on using a custom pointer, refer to [`Pointing devices`](https://developer.apple.com/design/Human-Interface-Guidelines/pointing-devices) in the Human Interface Guidelines.

You may apply this pointer style to a single view or a view hierarchy using the [`pointerStyle(_:)`](view/pointerstyle(_:).md) modifier.

## Parameters

- `shape`: The pointer shape.
- `eoFill`: A Boolean that indicates whether the shape is interpreted   with the even-odd winding number rule.
- `size`: The size of the pointer shape.

## See Also

- [static image(_:hotSpot:)](pointerstyle/image(_:hotspot:).md)
  Initializes a pointer style with a given image and hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/shape(_:eofill:size:))*