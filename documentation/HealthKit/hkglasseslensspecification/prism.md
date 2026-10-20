# prism

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

An object that contains information about the eye alignment correction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var prism: HKVisionPrism? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKVisionPrism * prism;
```

## See Also

### Accessing the specification’s data
- [var farPupillaryDistance: HKQuantity?](./farpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at an object far away, measured in mm.
- [var nearPupillaryDistance: HKQuantity?](./nearpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at a nearby object, measured in mm.
- [var vertexDistance: HKQuantity?](./vertexdistance.md)
  The distance between the back of the lens and the eye, measured in mm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkglasseslensspecification/prism)*