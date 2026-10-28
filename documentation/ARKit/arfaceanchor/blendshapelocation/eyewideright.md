# eyeWideRight

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The coefficient describing a widening of the eyelids around the right eye.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static let eyeWideRight: ARFaceAnchor.BlendShapeLocation
```

```c
extern ARBlendShapeLocation const ARBlendShapeLocationEyeWideRight;
```

## Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](../../arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](../blendshapelocation.md) coefficients are set to `0.0`.

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2929214@2x.png)

## See Also

### Right Eye
- [static let eyeBlinkRight: ARFaceAnchor.BlendShapeLocation](./eyeblinkright.md)
  The coefficient describing closure of the eyelids over the right eye.
- [static let eyeLookDownRight: ARFaceAnchor.BlendShapeLocation](./eyelookdownright.md)
  The coefficient describing movement of the right eyelids consistent with a downward gaze.
- [static let eyeLookInRight: ARFaceAnchor.BlendShapeLocation](./eyelookinright.md)
  The coefficient describing movement of the right eyelids consistent with a leftward gaze.
- [static let eyeLookOutRight: ARFaceAnchor.BlendShapeLocation](./eyelookoutright.md)
  The coefficient describing movement of the right eyelids consistent with a rightward gaze.
- [static let eyeLookUpRight: ARFaceAnchor.BlendShapeLocation](./eyelookupright.md)
  The coefficient describing movement of the right eyelids consistent with an upward gaze.
- [static let eyeSquintRight: ARFaceAnchor.BlendShapeLocation](./eyesquintright.md)
  The coefficient describing contraction of the face around the right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyewideright)*