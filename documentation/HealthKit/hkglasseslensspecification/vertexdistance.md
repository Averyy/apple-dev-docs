# vertexDistance

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The distance between the back of the lens and the eye, measured in mm.

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
var vertexDistance: HKQuantity? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * vertexDistance;
```

## Discussion

This property’s range is from 12 to 14 mm.

## See Also

### Accessing the specification’s data
- [var farPupillaryDistance: HKQuantity?](./farpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at an object far away, measured in mm.
- [var nearPupillaryDistance: HKQuantity?](./nearpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at a nearby object, measured in mm.
- [var prism: HKVisionPrism?](./prism.md)
  An object that contains information about the eye alignment correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkglasseslensspecification/vertexdistance)*