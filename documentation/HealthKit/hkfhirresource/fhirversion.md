# fhirVersion

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The FHIR version used by this resource.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var fhirVersion: HKFHIRVersion { get }
```

```objc
@property (copy, readonly) HKFHIRVersion * FHIRVersion;
```

## See Also

### Accessing FHIR Data
- [var identifier: String](./identifier.md)
  The value from the FHIR resource’s `id` field.
- [class HKFHIRVersion](../hkfhirversion.md)
  The FHIR version.
- [var resourceType: HKFHIRResourceType](./resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [struct HKFHIRResourceType](../hkfhirresourcetype.md)
  The FHIR resource types supported in HealthKit.
- [var sourceURL: URL?](./sourceurl.md)
  The full URL for the source of the FHIR resource.
- [var data: Data](./data.md)
  The JSON representation of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresource/fhirversion)*