# rotationEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Rotates content in two dimensions around the specified point.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some HoverEffectContent
```

#### Return Value

A rotation effect.

#### Discussion

This effect rotates the content around the axis that points out of the xy-plane. It has no effect on the content’s frame.

## Parameters

- `angle`: The angle by which to rotate the content.
- `anchor`: A unit point within the content about which to   perform the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/rotationeffect(_:anchor:))*