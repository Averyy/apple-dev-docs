# ARFaceAnchor.BlendShapeLocation

**Framework**: Arkit  
**Kind**: struct

Identifiers for specific facial features, for use with coefficients describing the relative movements of those features.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct BlendShapeLocation
```

#### Discussion

The [`blendShapes`](arfaceanchor/blendshapes.md) dictionary provided by an [`ARFaceAnchor`](arfaceanchor.md) object describes the facial expression of a detected face in terms of the movements of specific facial features. For each key in the dictionary, the corresponding value is a floating point number indicating the current position of that feature relative to its neutral configuration, ranging from `0.0` (neutral) to `1.0` (maximum movement).

ARKit provides many blend shape coefficients, resulting in a detailed model of a facial expression; however, you can use as many or as few of the coefficients as you desire to create a visual effect. For example, you might animate a simple cartoon character using only the [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md), [`eyeBlinkLeft`](arfaceanchor/blendshapelocation/eyeblinkleft.md), and [`eyeBlinkRight`](arfaceanchor/blendshapelocation/eyeblinkright.md) coefficients. A professional 3D artist could create a detailed character model rigged for realistic animation using a larger set, or the entire set, of coefficients.

> **Note**:  In the naming of blend shape coefficients, the left and right directions are relative to the face. That is, the [`eyeBlinkRight`](arfaceanchor/blendshapelocation/eyeblinkright.md) coefficient refers to the face’s right eye. ARKit views running a face-tracking session mirror the camera image, so the face’s right eye appears on the right side in the view.

## Topics

### Left Eye
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
- [static let eyeWideLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyewideleft.md)
  The coefficient describing a widening of the eyelids around the left eye.
### Right Eye
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
- [static let eyeWideRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/eyewideright.md)
  The coefficient describing a widening of the eyelids around the right eye.
### Mouth and Jaw
- [static let jawForward: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawforward.md)
  The coefficient describing forward movement of the lower jaw.
- [static let jawLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawleft.md)
  The coefficient describing leftward movement of the lower jaw.
- [static let jawRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawright.md)
  The coefficient describing rightward movement of the lower jaw.
- [static let jawOpen: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/jawopen.md)
  The coefficient describing an opening of the lower jaw.
- [static let mouthClose: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthclose.md)
  The coefficient describing closure of the lips .
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
- [static let mouthStretchRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthstretchright.md)
  The coefficient describing rightward movement of the left corner of the mouth.
- [static let mouthRollLower: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthrolllower.md)
  The coefficient describing movement of the lower lip toward the inside of the mouth.
- [static let mouthRollUpper: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthrollupper.md)
  The coefficient describing movement of the upper lip toward the inside of the mouth.
- [static let mouthShrugLower: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthshruglower.md)
  The coefficient describing outward movement of the lower lip.
- [static let mouthShrugUpper: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthshrugupper.md)
  The coefficient describing outward movement of the upper lip.
- [static let mouthPressLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthpressleft.md)
  The coefficient describing upward compression of the lower lip on the left side.
- [static let mouthPressRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthpressright.md)
  The coefficient describing upward compression of the lower lip on the right side.
- [static let mouthLowerDownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthlowerdownleft.md)
  The coefficient describing downward movement of the lower lip on the left side.
- [static let mouthLowerDownRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthlowerdownright.md)
  The coefficient describing downward movement of the lower lip on the right side.
- [static let mouthUpperUpLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthupperupleft.md)
  The coefficient describing upward movement of the upper lip on the left side.
- [static let mouthUpperUpRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/mouthupperupright.md)
  The coefficient describing upward movement of the upper lip on the right side.
### Eyebrows, Cheeks, and Nose
- [static let browDownLeft: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browdownleft.md)
  The coefficient describing downward movement of the outer portion of the left eyebrow.
- [static let browDownRight: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browdownright.md)
  The coefficient describing downward movement of the outer portion of the right eyebrow.
- [static let browInnerUp: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/browinnerup.md)
  The coefficient describing upward movement of the inner portion of both eyebrows.
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
### Tongue
- [static let tongueOut: ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation/tongueout.md)
  The coefficient describing extension of the tongue.
### Creating a Blend Shape Location
- [init(rawValue: String)](arfaceanchor/blendshapelocation/init(rawvalue:).md)
  Creates a blend shape location.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var blendShapes: [ARFaceAnchor.BlendShapeLocation : NSNumber]](arfaceanchor/blendshapes.md)
  A dictionary of named coefficients representing the detected facial expression in terms of the movement of specific facial features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ARKit/arfaceanchor/blendshapelocation)*