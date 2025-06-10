# rotation3DLayout(_:axis:)

**Framework**: Assignables  
**Kind**: method

Rotates a view with impacts to its frame in a containing layout

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func rotation3DLayout(_ angle: Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat)) -> some View
```

#### Discussion

The following example will rotate the top plane by 45 degrees while adjusting its frame to account for this rotation. The VStack sizes to fit the rotated and standard models.

```None
VStack {
    Model3D(named: "plane")
        .rotation3DLayout(.degrees(45), axis: (x: 0, y: 0, z: 1))
    Model3D(named: "plane")
```

}

The layout system will use a bounding box that completely contains the rotated view, meaning this modifier can change the size of the view it is applied to.

## Parameters

- `angle`: The angle by which to rotate the view and its frame.
- `axis`: The axis of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/rotation3dlayout(_:axis:)-6z69x)*