# browInnerUp

**Framework**: ARKit  
**Kind**: property

The coefficient describing upward movement of the inner portion of both eyebrows.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let browInnerUp: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficients are set to `0.0`.

![None](https://docs-assets.developer.apple.com/published/d124c94a357c86c3e74a4f018ad2ada0/media-2929223%402x.png)

## See Also

- [static let browDownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browdownleft.md)
  The coefficient describing downward movement of the outer portion of the left eyebrow.
- [static let browDownRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browdownright.md)
  The coefficient describing downward movement of the outer portion of the right eyebrow.
- [static let browOuterUpLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browouterupleft.md)
  The coefficient describing upward movement of the outer portion of the left eyebrow.
- [static let browOuterUpRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browouterupright.md)
  The coefficient describing upward movement of the outer portion of the right eyebrow.
- [static let cheekPuff: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/cheekpuff.md)
  The coefficient describing outward movement of both cheeks.
- [static let cheekSquintLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/cheeksquintleft.md)
  The coefficient describing upward movement of the cheek around and below the left eye.
- [static let cheekSquintRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/cheeksquintright.md)
  The coefficient describing upward movement of the cheek around and below the right eye.
- [static let noseSneerLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/nosesneerleft.md)
  The coefficient describing a raising of the left side of the nose around the nostril.
- [static let noseSneerRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/nosesneerright.md)
  The coefficient describing a raising of the right side of the nose around the nostril.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/browinnerup)*