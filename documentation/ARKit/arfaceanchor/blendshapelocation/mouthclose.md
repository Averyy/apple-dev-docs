# mouthClose

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The coefficient describing closure of the lips *independent of jaw position*.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static let mouthClose: ARFaceAnchor.BlendShapeLocation
```

```c
extern ARBlendShapeLocation const ARBlendShapeLocationMouthClose;
```

## Discussion

This coefficient describes a closing of the lips without relation to the position of the jaw (the [`jawOpen`](./jawopen.md) coefficient), so some values of the [`mouthClose`](./mouthclose.md) coefficient can produce unrealistic facial expressions unless other coefficients are also set to realistic values.

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](../../arscnfacegeometry.md)) in three states:

1. A neutral face (all [`ARFaceAnchor.BlendShapeLocation`](../blendshapelocation.md) coefficient values at `0.0`, including both [`jawOpen`](./jawopen.md) and [`mouthClose`](./mouthclose.md))
2. Setting only the [`jawOpen`](./jawopen.md) coefficient to `1.0`, while keeping all other coefficient values (including [`mouthClose`](./mouthclose.md)) at `0.0`
3. Setting both the [`jawOpen`](./jawopen.md) and [`mouthClose`](./mouthclose.md) coefficients to `1.0`, while keeping all other coefficient values at `0.0`

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2930045@2x.png)

## See Also

### Mouth and Jaw
- [static let jawForward: ARFaceAnchor.BlendShapeLocation](./jawforward.md)
  The coefficient describing forward movement of the lower jaw.
- [static let jawLeft: ARFaceAnchor.BlendShapeLocation](./jawleft.md)
  The coefficient describing leftward movement of the lower jaw.
- [static let jawRight: ARFaceAnchor.BlendShapeLocation](./jawright.md)
  The coefficient describing rightward movement of the lower jaw.
- [static let jawOpen: ARFaceAnchor.BlendShapeLocation](./jawopen.md)
  The coefficient describing an opening of the lower jaw.
- [static let mouthFunnel: ARFaceAnchor.BlendShapeLocation](./mouthfunnel.md)
  The coefficient describing contraction of both lips into an open shape.
- [static let mouthPucker: ARFaceAnchor.BlendShapeLocation](./mouthpucker.md)
  The coefficient describing contraction and compression of both closed lips.
- [static let mouthLeft: ARFaceAnchor.BlendShapeLocation](./mouthleft.md)
  The coefficient describing leftward movement of both lips together.
- [static let mouthRight: ARFaceAnchor.BlendShapeLocation](./mouthright.md)
  The coefficient describing rightward movement of both lips together.
- [static let mouthSmileLeft: ARFaceAnchor.BlendShapeLocation](./mouthsmileleft.md)
  The coefficient describing upward movement of the left corner of the mouth.
- [static let mouthSmileRight: ARFaceAnchor.BlendShapeLocation](./mouthsmileright.md)
  The coefficient describing upward movement of the right corner of the mouth.
- [static let mouthFrownLeft: ARFaceAnchor.BlendShapeLocation](./mouthfrownleft.md)
  The coefficient describing downward movement of the left corner of the mouth.
- [static let mouthFrownRight: ARFaceAnchor.BlendShapeLocation](./mouthfrownright.md)
  The coefficient describing downward movement of the right corner of the mouth.
- [static let mouthDimpleLeft: ARFaceAnchor.BlendShapeLocation](./mouthdimpleleft.md)
  The coefficient describing backward movement of the left corner of the mouth.
- [static let mouthDimpleRight: ARFaceAnchor.BlendShapeLocation](./mouthdimpleright.md)
  The coefficient describing backward movement of the right corner of the mouth.
- [static let mouthStretchLeft: ARFaceAnchor.BlendShapeLocation](./mouthstretchleft.md)
  The coefficient describing leftward movement of the left corner of the mouth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/mouthclose)*