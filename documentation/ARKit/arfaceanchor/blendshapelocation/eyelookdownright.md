# eyeLookDownRight

**Framework**: ARKit  
**Kind**: property

The coefficient describing movement of the right eyelids consistent with a downward gaze.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let eyeLookDownRight: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficients are set to `0.0`.

![None](https://docs-assets.developer.apple.com/published/5fdfdb5159bcce50065f1b2f2630be68/media-2929212%402x.png)

## See Also

- [static let eyeBlinkRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyeblinkright.md)
  The coefficient describing closure of the eyelids over the right eye.
- [static let eyeLookInRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookinright.md)
  The coefficient describing movement of the right eyelids consistent with a leftward gaze.
- [static let eyeLookOutRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookoutright.md)
  The coefficient describing movement of the right eyelids consistent with a rightward gaze.
- [static let eyeLookUpRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookupright.md)
  The coefficient describing movement of the right eyelids consistent with an upward gaze.
- [static let eyeSquintRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyesquintright.md)
  The coefficient describing contraction of the face around the right eye.
- [static let eyeWideRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyewideright.md)
  The coefficient describing a widening of the eyelids around the right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyelookdownright)*