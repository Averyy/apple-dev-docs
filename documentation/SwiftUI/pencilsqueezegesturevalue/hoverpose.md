# hoverPose

**Framework**: SwiftUI  
**Kind**: property

The location and distance of an Apple Pencil hovering in the area above the view’s bounds when the squeeze gesture occurred.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
let hoverPose: PencilHoverPose?
```

#### Discussion

If the Apple Pencil was hovering in the area above the view’s bounds when the user squeezed their Apple Pencil, this property describes its pose relative to that view.

Conversely, if the Apple Pencil wasn’t hovering in the area above the view’s bounds or if the device can’t detect a hovering Apple Pencil, this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilsqueezegesturevalue/hoverpose)*