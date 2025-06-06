# outerAngle

**Framework**: PHASE  
**Kind**: property

An angle, in degrees, that determines the size of the audio emitting area outside the cone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var outerAngle: Double { get }
```

#### Discussion

To set this property, call [`setAngles(innerAngle:outerAngle:)`](phaseconedirectivitymodelsubbandparameters/setangles(innerangle:outerangle:).md).

## See Also

- [var innerAngle: Double](phaseconedirectivitymodelsubbandparameters/innerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area inside the cone.
- [var outerGain: Double](phaseconedirectivitymodelsubbandparameters/outergain.md)
  The loudness of the audio the outside area of the cone emits.
- [func setAngles(innerAngle: Double, outerAngle: Double)](phaseconedirectivitymodelsubbandparameters/setangles(innerangle:outerangle:).md)
  Configures a focus area for cone-based sound directivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelsubbandparameters/outerangle)*