# outerGain

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The loudness of the audio the outside area of the cone emits.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var outerGain: Double { get set }
```

```objc
@property (nonatomic) double outerGain;
```

#### Discussion

The framework clamps the value of this property to the range `[0,` `1]`, where `0` silences loudness and `1` doesn’t modify loudness.

## See Also

### Shaping Directivity
- [var innerAngle: Double](./innerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area inside the cone.
- [var outerAngle: Double](./outerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area outside the cone.
- [func setAngles(innerAngle: Double, outerAngle: Double)](./setangles%28innerangle,outerangle%29.md)
  Configures a focus area for cone-based sound directivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelsubbandparameters/outergain)*