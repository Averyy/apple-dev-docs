# eyeLookOutLeft

**Framework**: ARKit  
**Kind**: property

The coefficient describing movement of the left eyelids consistent with a leftward gaze.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let eyeLookOutLeft: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficients are set to `0.0`.

![None](https://docs-assets.developer.apple.com/published/dae99f0203fd63ec477fd23957637244/media-2929206%402x.png)

## See Also

- [static let eyeBlinkLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyeblinkleft.md)
  The coefficient describing closure of the eyelids over the left eye.
- [static let eyeLookDownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookdownleft.md)
  The coefficient describing movement of the left eyelids consistent with a downward gaze.
- [static let eyeLookInLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookinleft.md)
  The coefficient describing movement of the left eyelids consistent with a rightward gaze.
- [static let eyeLookUpLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookupleft.md)
  The coefficient describing movement of the left eyelids consistent with an upward gaze.
- [static let eyeSquintLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyesquintleft.md)
  The coefficient describing contraction of the face around the left eye.
- [static let eyeWideLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyewideleft.md)
  The coefficient describing a widening of the eyelids around the left eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyelookoutleft)*