# init(rightEyeSpecification:leftEyeSpecification:dateIssued:expirationDate:device:metadata:)

**Framework**: HealthKit  
**Kind**: init

Creates a new glasses prescription sample.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init(rightEyeSpecification: HKGlassesLensSpecification?, leftEyeSpecification: HKGlassesLensSpecification?, dateIssued: Date, expirationDate: Date?, device: HKDevice?, metadata: [String : Any]?)
```

## Parameters

- `rightEyeSpecification`: The lens specification for the right eye.
- `leftEyeSpecification`: The lens specification for the left eye.
- `dateIssued`: The date when the doctor issued the prescription.
- `expirationDate`: The date when the prescription expires.
- `device`: The device that generated the sample.
- `metadata`: Additional metadata about the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkglassesprescription/init(righteyespecification:lefteyespecification:dateissued:expirationdate:device:metadata:))*