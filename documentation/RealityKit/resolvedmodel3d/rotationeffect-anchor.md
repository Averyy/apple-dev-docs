# rotationEffect(_:anchor:)

**Framework**: RealityKit  
**Kind**: method

Rotates a view’s rendered output in two dimensions around the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func rotationEffect(_ angle: Angle, anchor: UnitPoint = .center) -> some View
```

#### Return Value

A view with rotated content.

#### Discussion

This modifier rotates the view’s content around the axis that points out of the xy-plane. It has no effect on the view’s frame. The following code rotates text by 22˚ and then draws a border around the modified view to show that the frame remains unchanged by the rotation modifier:

```None
Text("Rotation by passing an angle in degrees")
    .rotationEffect(.degrees(22))
    .border(Color.gray)
```

## Parameters

- `angle`: The angle by which to rotate the view.
- `anchor`: A unit point within the view about which to   perform the rotation. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/rotationeffect(_:anchor:))*