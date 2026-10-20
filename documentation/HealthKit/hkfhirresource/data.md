# data

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSData * data;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Accessing FHIR Data
- [var identifier: String](./identifier.md)
  The value from the FHIR resource’s `id` field.
- [var fhirVersion: HKFHIRVersion](./fhirversion.md)
  The FHIR version used by this resource.
- [class HKFHIRVersion](../hkfhirversion.md)
  The FHIR version.
- [var resourceType: HKFHIRResourceType](./resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [struct HKFHIRResourceType](../hkfhirresourcetype.md)
  The FHIR resource types supported in HealthKit.
- [var sourceURL: URL?](./sourceurl.md)
  The full URL for the source of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresource/data)*