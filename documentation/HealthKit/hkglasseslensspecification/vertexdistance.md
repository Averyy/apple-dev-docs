# vertexDistance

**Framework**: HealthKit  
**Kind**: property

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

#### Discussion

This property’s range is from 12 to 14 mm.

## See Also

- [var farPupillaryDistance: HKQuantity?](hkglasseslensspecification/farpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at an object far away, measured in mm.
- [var nearPupillaryDistance: HKQuantity?](hkglasseslensspecification/nearpupillarydistance.md)
  The distance between the pupil and the center of the nose when looking at a nearby object, measured in mm.
- [var prism: HKVisionPrism?](hkglasseslensspecification/prism.md)
  An object that contains information about the eye alignment correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkglasseslensspecification/vertexdistance)*