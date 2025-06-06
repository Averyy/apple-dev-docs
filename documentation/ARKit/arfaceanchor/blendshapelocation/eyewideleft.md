# eyeWideLeft

**Framework**: ARKit  
**Kind**: property

The coefficient describing a widening of the eyelids around the left eye.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let eyeWideLeft: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficients are set to `0.0`.

![None](https://docs-assets.developer.apple.com/published/87ae86438bcc0b2610ab22138ae40668/media-2929207%402x.png)

## See Also

- [static let eyeBlinkLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyeblinkleft.md)
  The coefficient describing closure of the eyelids over the left eye.
- [static let eyeLookDownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookdownleft.md)
  The coefficient describing movement of the left eyelids consistent with a downward gaze.
- [static let eyeLookInLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookinleft.md)
  The coefficient describing movement of the left eyelids consistent with a rightward gaze.
- [static let eyeLookOutLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookoutleft.md)
  The coefficient describing movement of the left eyelids consistent with a leftward gaze.
- [static let eyeLookUpLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookupleft.md)
  The coefficient describing movement of the left eyelids consistent with an upward gaze.
- [static let eyeSquintLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyesquintleft.md)
  The coefficient describing contraction of the face around the left eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyewideleft)*