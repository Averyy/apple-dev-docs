# identifier

**Framework**: HealthKit  
**Kind**: property

The value from the FHIR resource’s `id` field.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

#### Discussion

This identifier is only unique for a particular resource type from a given source. To uniquely identify a FHIR resource, you must compare the [`identifier`](hkfhirresource/identifier.md) and [`resourceType`](hkfhirresource/resourcetype.md) properties from the [`HKFHIRResource`](hkfhirresource.md) object and the [`bundleIdentifier`](hksource/bundleidentifier.md) property from the clinical record’s [`source`](hkobject/source.md).

## See Also

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
- [var data: Data](hkfhirresource/data.md)
  The JSON representation of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresource/identifier)*