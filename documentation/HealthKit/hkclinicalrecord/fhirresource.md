# fhirResource

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The Fast Healthcare Interoperability Resources (FHIR) data for this record.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var fhirResource: HKFHIRResource? { get }
```

```objc
@property (copy, readonly, nullable) HKFHIRResource * FHIRResource;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Accessing Clinical Record Data
- [var clinicalType: HKClinicalType](./clinicaltype.md)
  An identifier that indicates the type of record, such as an allergic reaction, a lab result, or a medical procedure.
- [var displayName: String](./displayname.md)
  The primary display name as shown in the Health app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalrecord/fhirresource)*