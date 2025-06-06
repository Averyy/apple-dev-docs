# eyeWideRight

**Framework**: ARKit  
**Kind**: property

The coefficient describing a widening of the eyelids around the right eye.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let eyeWideRight: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficients are set to `0.0`.

![None](https://docs-assets.developer.apple.com/published/13a79b8fe2350e4cd43e5099b66e790a/media-2929214%402x.png)

## See Also

- [static let eyeBlinkRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyeblinkright.md)
  The coefficient describing closure of the eyelids over the right eye.
- [static let eyeLookDownRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookdownright.md)
  The coefficient describing movement of the right eyelids consistent with a downward gaze.
- [static let eyeLookInRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookinright.md)
  The coefficient describing movement of the right eyelids consistent with a leftward gaze.
- [static let eyeLookOutRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookoutright.md)
  The coefficient describing movement of the right eyelids consistent with a rightward gaze.
- [static let eyeLookUpRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyelookupright.md)
  The coefficient describing movement of the right eyelids consistent with an upward gaze.
- [static let eyeSquintRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyesquintright.md)
  The coefficient describing contraction of the face around the right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyewideright)*