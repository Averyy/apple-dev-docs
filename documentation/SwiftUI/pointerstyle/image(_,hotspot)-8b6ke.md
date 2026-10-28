# image(_:hotSpot:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Initializes a pointer style with a given image resource and hot spot.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func image(_ resource: ImageResource, hotSpot: UnitPoint) -> PointerStyle
```

**Other overloads**:

```swift
static func image(_ image: Image, hotSpot: UnitPoint) -> PointerStyle
```

## Discussion

The hot spot is the part of the pointer that must be positioned over an onscreen element for clicking to have an effect.

For guidance on using a custom pointer, refer to [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) in the Human Interface Guidelines.

You may apply this pointer style to a single view or a view hierarchy using the [`pointerStyle(_:)`](../view/pointerstyle%28_%29.md) modifier.

## Parameters

- `hotSpot`: The point on the image that represents the location from which the pointer interaction occurs. For example, the hot spot of an arrow-shaped pointer is the tip of the arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/image(_:hotspot:)-8b6ke)*