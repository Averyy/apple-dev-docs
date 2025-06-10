# rotation3DLayout(_:)

**Framework**: Assignables  
**Kind**: method

Rotates a view with impacts to its frame in a containing layout

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func rotation3DLayout(_ rotation: Rotation3D) -> some View
```

#### Discussion

The following example will rotate the top plane by 45 degrees while adjusting its frame to account for this rotation. The VStack sizes to fit the rotated and standard models.

```None
VStack {
    Model3D(named: "plane")
        .rotation3DLayout(Rotation3D(angle: .degrees(45), axis: .z))
    Model3D(named: "plane")
```

}

The layout system will use a bounding box that completely contains the rotated view, meaning this modifier can change the size of the view it is applied to.

## Parameters

- `rotation`: A rotation to apply to the view and its frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/rotation3dlayout(_:))*