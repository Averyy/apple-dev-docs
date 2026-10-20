# mouthFrownLeft

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The coefficient describing downward movement of the left corner of the mouth.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static let mouthFrownLeft: ARFaceAnchor.BlendShapeLocation
```

```c
extern ARBlendShapeLocation const ARBlendShapeLocationMouthFrownLeft;
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](../../arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](../blendshapelocation.md) coefficients are set to `0.0`.

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2930072@2x.png)

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
- [static let mouthClose: ARFaceAnchor.BlendShapeLocation](./mouthclose.md)
  The coefficient describing closure of the lips *independent of jaw position*.
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
- [static let mouthFrownRight: ARFaceAnchor.BlendShapeLocation](./mouthfrownright.md)
  The coefficient describing downward movement of the right corner of the mouth.
- [static let mouthDimpleLeft: ARFaceAnchor.BlendShapeLocation](./mouthdimpleleft.md)
  The coefficient describing backward movement of the left corner of the mouth.
- [static let mouthDimpleRight: ARFaceAnchor.BlendShapeLocation](./mouthdimpleright.md)
  The coefficient describing backward movement of the right corner of the mouth.
- [static let mouthStretchLeft: ARFaceAnchor.BlendShapeLocation](./mouthstretchleft.md)
  The coefficient describing leftward movement of the left corner of the mouth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/mouthfrownleft)*