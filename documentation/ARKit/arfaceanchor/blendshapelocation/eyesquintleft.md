# eyeSquintLeft

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The coefficient describing contraction of the face around the left eye.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static let eyeSquintLeft: ARFaceAnchor.BlendShapeLocation
```

```c
extern ARBlendShapeLocation const ARBlendShapeLocationEyeSquintLeft;
```

#### Discussion

The figure below shows a face geometry (see [`ARSCNFaceGeometry`](../../arscnfacegeometry.md)) in two states, demonstrating values of `0.0` and `1.0` for this coefficient. In both states, the values for all other [`ARFaceAnchor.BlendShapeLocation`](../blendshapelocation.md) coefficients are set to `0.0`.

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2929201@2x.png)

## See Also

### Left Eye
- [static let eyeBlinkLeft: ARFaceAnchor.BlendShapeLocation](./eyeblinkleft.md)
  The coefficient describing closure of the eyelids over the left eye.
- [static let eyeLookDownLeft: ARFaceAnchor.BlendShapeLocation](./eyelookdownleft.md)
  The coefficient describing movement of the left eyelids consistent with a downward gaze.
- [static let eyeLookInLeft: ARFaceAnchor.BlendShapeLocation](./eyelookinleft.md)
  The coefficient describing movement of the left eyelids consistent with a rightward gaze.
- [static let eyeLookOutLeft: ARFaceAnchor.BlendShapeLocation](./eyelookoutleft.md)
  The coefficient describing movement of the left eyelids consistent with a leftward gaze.
- [static let eyeLookUpLeft: ARFaceAnchor.BlendShapeLocation](./eyelookupleft.md)
  The coefficient describing movement of the left eyelids consistent with an upward gaze.
- [static let eyeWideLeft: ARFaceAnchor.BlendShapeLocation](./eyewideleft.md)
  The coefficient describing a widening of the eyelids around the left eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation/eyesquintleft)*