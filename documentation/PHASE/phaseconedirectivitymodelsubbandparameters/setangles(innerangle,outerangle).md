# setAngles(innerAngle:outerAngle:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Configures a focus area for cone-based sound directivity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setAngles(innerAngle: Double, outerAngle: Double)
```

```objc
- (void) setInnerAngle:(double) innerAngle outerAngle:(double) outerAngle;
```

#### Discussion

The default value for each angle is `360.0`. The outer angle needs to be greater than or equal to the inner angle.

## Parameters

- `innerAngle`: An angle that determines the size of the audio emitting area inside the cone.
- `outerAngle`: An angle that determines the size of the audio emitting area outside the cone.

## See Also

### Shaping Directivity
- [var innerAngle: Double](./innerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area inside the cone.
- [var outerAngle: Double](./outerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area outside the cone.
- [var outerGain: Double](./outergain.md)
  The loudness of the audio the outside area of the cone emits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelsubbandparameters/setangles(innerangle:outerangle:))*