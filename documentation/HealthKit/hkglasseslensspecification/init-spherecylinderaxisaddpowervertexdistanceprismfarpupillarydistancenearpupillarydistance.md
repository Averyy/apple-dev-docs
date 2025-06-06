# init(sphere:cylinder:axis:addPower:vertexDistance:prism:farPupillaryDistance:nearPupillaryDistance:)

**Framework**: HealthKit  
**Kind**: init

Creates a new glasses lens specification, containing the prescription data for one eye.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(sphere: HKQuantity, cylinder: HKQuantity?, axis: HKQuantity?, addPower: HKQuantity?, vertexDistance: HKQuantity?, prism: HKVisionPrism?, farPupillaryDistance: HKQuantity?, nearPupillaryDistance: HKQuantity?)
```

## Parameters

- `sphere`: The correction for farsightedness, measured in   units. The range is -10.5 to +6.5.
- `cylinder`: Part of the correction for astigmatism. This property measures the strength of the correction in   units. The range is -3.0 to 3.0.
- `axis`: Part of the correction for astigmatism. This property measures the orientation of the correction in   units.
- `addPower`: The correction for nearsightedness, measured in   units. The range is from 0.25 to 2.5. The right and left eyes should have the same value.
- `vertexDistance`: The distance between the back of the lens and the eye, measured in mm. The range is 12 to 14 mm.
- `prism`: An object that contains information about the correction for eye alignment. For more information, see  .
- `farPupillaryDistance`: The distance between the pupil and the center of the nose when looking at an object far away, measured in mm.
- `nearPupillaryDistance`: The distance between the pupil and the center of the nose when looking at a nearby object, measured in mm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkglasseslensspecification/init(sphere:cylinder:axis:addpower:vertexdistance:prism:farpupillarydistance:nearpupillarydistance:))*