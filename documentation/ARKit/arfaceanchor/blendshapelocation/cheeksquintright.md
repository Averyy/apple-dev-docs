# cheekSquintRight

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The coefficient describing upward movement of the cheek around and below the right eye.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static let cheekSquintRight: ARFaceAnchor.BlendShapeLocation
```

```c
extern ARBlendShapeLocation const ARBlendShapeLocationCheekSquintRight;
```

## Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](../../arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](../blendshapelocation.md) coefficients are set to `0.0`.

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2930095@2x.png)

## See Also

### Eyebrows, Cheeks, and Nose
- [static let browDownLeft: ARFaceAnchor.BlendShapeLocation](./browdownleft.md)
  The coefficient describing downward movement of the outer portion of the left eyebrow.
- [static let browDownRight: ARFaceAnchor.BlendShapeLocation](./browdownright.md)
  The coefficient describing downward movement of the outer portion of the right eyebrow.
- [static let browInnerUp: ARFaceAnchor.BlendShapeLocation](./browinnerup.md)
  The coefficient describing upward movement of the inner portion of both eyebrows.
- [static let browOuterUpLeft: ARFaceAnchor.BlendShapeLocation](./browouterupleft.md)
  The coefficient describing upward movement of the outer portion of the left eyebrow.
- [static let browOuterUpRight: ARFaceAnchor.BlendShapeLocation](./browouterupright.md)
  The coefficient describing upward movement of the outer portion of the right eyebrow.
- [static let cheekPuff: ARFaceAnchor.BlendShapeLocation](./cheekpuff.md)
  The coefficient describing outward movement of both cheeks.
- [static let cheekSquintLeft: ARFaceAnchor.BlendShapeLocation](./cheeksquintleft.md)
  The coefficient describing upward movement of the cheek around and below the left eye.
- [static let noseSneerLeft: ARFaceAnchor.BlendShapeLocation](./nosesneerleft.md)
  The coefficient describing a raising of the left side of the nose around the nostril.
- [static let noseSneerRight: ARFaceAnchor.BlendShapeLocation](./nosesneerright.md)
  The coefficient describing a raising of the right side of the nose around the nostril.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/cheeksquintright)*