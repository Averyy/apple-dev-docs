# data

**Framework**: HealthKit  
**Kind**: property

The JSON representation of the FHIR resource.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var data: Data { get }
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

## See Also

- [var identifier: String](hkfhirresource/identifier.md)
  The value from the FHIR resource’s `id` field.
- [var fhirVersion: HKFHIRVersion](hkfhirresource/fhirversion.md)
  The FHIR version used by this resource.
- [class HKFHIRVersion](hkfhirversion.md)
  The FHIR version.
- [var resourceType: HKFHIRResourceType](hkfhirresource/resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [struct HKFHIRResourceType](hkfhirresourcetype.md)
  The FHIR resource types supported in HealthKit.
- [var sourceURL: URL?](hkfhirresource/sourceurl.md)
  The full URL for the source of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresource/data)*