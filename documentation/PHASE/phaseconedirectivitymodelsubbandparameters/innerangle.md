# innerAngle

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

An angle, in degrees, that determines the size of the audio emitting area inside the cone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var innerAngle: Double { get }
```

```objc
@property (readonly) double innerAngle;
```

## Discussion

To set this property, call [`setAngles(innerAngle:outerAngle:)`](./setangles%28innerangle,outerangle%29.md).

## See Also

### Shaping Directivity
- [var outerAngle: Double](./outerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area outside the cone.
- [var outerGain: Double](./outergain.md)
  The loudness of the audio the outside area of the cone emits.
- [func setAngles(innerAngle: Double, outerAngle: Double)](./setangles%28innerangle,outerangle%29.md)
  Configures a focus area for cone-based sound directivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelsubbandparameters/innerangle)*