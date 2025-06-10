# HKFHIRRelease

**Framework**: HealthKit  
**Kind**: struct

Official releases of the FHIR specification.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKFHIRRelease
```

#### Overview

Each release can have multiple versions.

## Topics

### Releases
- [static let dstu2: HKFHIRRelease](hkfhirrelease/dstu2.md)
  The Second Draft Standard for Trial Use (DSTU2) release.
- [static let r4: HKFHIRRelease](hkfhirrelease/r4.md)
  The Release 4 (R4) release.
- [static let unknown: HKFHIRRelease](hkfhirrelease/unknown.md)
  An unknown release.
### Initializers
- [init(rawValue: String)](hkfhirrelease/init(rawvalue:).md)
  Creates a new release from the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var fhirRelease: HKFHIRRelease](hkfhirversion/fhirrelease.md)
  An official release of the FHIR specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirrelease)*