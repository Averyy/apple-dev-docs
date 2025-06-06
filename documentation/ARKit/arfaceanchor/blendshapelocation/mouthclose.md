# mouthClose

**Framework**: ARKit  
**Kind**: property

The coefficient describing closure of the lips .

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let mouthClose: ARFaceAnchor.BlendShapeLocation
```

#### Discussion

This coefficient describes a closing of the lips without relation to the position of the jaw (the [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md) coefficient), so some values of the [`mouthClose`](arfaceanchor/blendshapelocation/mouthclose.md) coefficient can produce unrealistic facial expressions unless other coefficients are also set to realistic values.

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](arscnfacegeometry.md)) in three states:

1. A neutral face (all [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) coefficient values at `0.0`, including both [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md) and [`mouthClose`](arfaceanchor/blendshapelocation/mouthclose.md))
2. Setting only the [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md) coefficient to `1.0`, while keeping all other coefficient values (including [`mouthClose`](arfaceanchor/blendshapelocation/mouthclose.md)) at `0.0`
3. Setting both the [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md) and [`mouthClose`](arfaceanchor/blendshapelocation/mouthclose.md) coefficients to `1.0`, while keeping all other coefficient values at `0.0`

![None](https://docs-assets.developer.apple.com/published/6c619637abe04b4af93ba25b4f13a950/media-2930045%402x.png)

## See Also

- [static let jawForward: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawforward.md)
  The coefficient describing forward movement of the lower jaw.
- [static let jawLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawleft.md)
  The coefficient describing leftward movement of the lower jaw.
- [static let jawRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawright.md)
  The coefficient describing rightward movement of the lower jaw.
- [static let jawOpen: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawopen.md)
  The coefficient describing an opening of the lower jaw.
- [static let mouthFunnel: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthfunnel.md)
  The coefficient describing contraction of both lips into an open shape.
- [static let mouthPucker: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthpucker.md)
  The coefficient describing contraction and compression of both closed lips.
- [static let mouthLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthleft.md)
  The coefficient describing leftward movement of both lips together.
- [static let mouthRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthright.md)
  The coefficient describing rightward movement of both lips together.
- [static let mouthSmileLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthsmileleft.md)
  The coefficient describing upward movement of the left corner of the mouth.
- [static let mouthSmileRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthsmileright.md)
  The coefficient describing upward movement of the right corner of the mouth.
- [static let mouthFrownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthfrownleft.md)
  The coefficient describing downward movement of the left corner of the mouth.
- [static let mouthFrownRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthfrownright.md)
  The coefficient describing downward movement of the right corner of the mouth.
- [static let mouthDimpleLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthdimpleleft.md)
  The coefficient describing backward movement of the left corner of the mouth.
- [static let mouthDimpleRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthdimpleright.md)
  The coefficient describing backward movement of the right corner of the mouth.
- [static let mouthStretchLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthstretchleft.md)
  The coefficient describing leftward movement of the left corner of the mouth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/mouthclose)*