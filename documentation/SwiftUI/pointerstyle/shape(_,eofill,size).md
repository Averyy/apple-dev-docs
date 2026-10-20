# shape(_:eoFill:size:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Initializes a pointer style with a given shape.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func shape(_ shape: some Shape, eoFill: Bool = false, size: CGSize) -> PointerStyle
```

#### Discussion

For guidance on using a custom pointer, refer to [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) in the Human Interface Guidelines.

You may apply this pointer style to a single view or a view hierarchy using the [`pointerStyle(_:)`](../view/pointerstyle%28_%29.md) modifier.

## Parameters

- `shape`: The pointer shape.
- `eoFill`: A Boolean that indicates whether the shape is interpreted with the even-odd winding number rule.
- `size`: The size of the pointer shape.

## See Also

### Creating custom pointer styles
- [static image(_:hotSpot:)](./image%28_,hotspot%29.md)
  Initializes a pointer style with a given image and hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/shape(_:eofill:size:))*