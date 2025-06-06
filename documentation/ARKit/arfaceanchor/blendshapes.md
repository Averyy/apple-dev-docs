# blendShapes

**Framework**: ARKit  
**Kind**: property

A dictionary of named coefficients representing the detected facial expression in terms of the movement of specific facial features.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var blendShapes: [ARFaceAnchor.BlendShapeLocation : NSNumber] { get }
```

#### Discussion

Each key in this dictionary (an [`ARFaceAnchor.BlendShapeLocation`](arfaceanchor/blendshapelocation.md) constant) represents one of many specific facial features recognized by ARKit. The corresponding value for each key is a floating point number indicating the current position of that feature relative to its neutral configuration, ranging from `0.0` (neutral) to `1.0` (maximum movement).

You can use blend shape coefficients to animate a 2D or 3D character in ways that follow the user’s facial expressions. ARKit provides many blend shape coefficients, resulting in a detailed model of a facial expression; however, you can use as many or as few of the coefficients as you desire to create a visual effect. For example, you might animate a simple cartoon character using only the [`jawOpen`](arfaceanchor/blendshapelocation/jawopen.md), [`eyeBlinkLeft`](arfaceanchor/blendshapelocation/eyeblinkleft.md), and [`eyeBlinkRight`](arfaceanchor/blendshapelocation/eyeblinkright.md) coefficients. A professional 3D artist could create a detailed character model rigged for realistic animation using a larger set, or the entire set, of coefficients.

You can also use blend shape coefficients to record a specific facial expression and reuse it later. The [`ARFaceGeometry`](arfacegeometry.md) [`init(blendShapes:)`](arfacegeometry/init(blendshapes:).md) initializer creates a detailed 3D mesh from a dictionary equivalent to this property’s value; the serialized form of a blend shapes dictionary is more portable than that of the face mesh those coefficients describe.

## See Also

- [ARFaceAnchor.BlendShapeLocation](arfaceanchor/blendshapelocation.md)
  Identifiers for specific facial features, for use with coefficients describing the relative movements of those features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapes)*