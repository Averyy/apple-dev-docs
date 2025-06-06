# HKFHIRVersion

**Framework**: HealthKit  
**Kind**: class

The FHIR version.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKFHIRVersion
```

#### Overview

Use an [`HKFHIRVersion`](hkfhirversion.md) instance to represent the version of the Fast Healthcare Interoperability Resources (FHIR) standard used to create a [`HKFHIRResource`](hkfhirresource.md) sample.

## Topics

### Creating Version Objects
- [convenience init(fromVersionString: String) throws](hkfhirversion/init(fromversionstring:).md)
  Creates an FHIR version object from a string representation of the version.
- [class func primaryDSTU2() -> Self](hkfhirversion/primarydstu2.md)
  Returns the primary Second Draft Standard for Trial Use (DSTU2) version.
- [class func primaryR4() -> Self](hkfhirversion/primaryr4.md)
  Returns the primary Release 4 (R4) version.
### Accessing Version Data
- [var majorVersion: Int](hkfhirversion/majorversion.md)
  The standard’s major version number.
- [var minorVersion: Int](hkfhirversion/minorversion.md)
  The standard’s minor version number.
- [var patchVersion: Int](hkfhirversion/patchversion.md)
  The standard’s patch version number.
- [var stringRepresentation: String](hkfhirversion/stringrepresentation.md)
  A string representation of the version.
### Accessing the Release
- [var fhirRelease: HKFHIRRelease](hkfhirversion/fhirrelease.md)
  An official release of the FHIR specification.
- [struct HKFHIRRelease](hkfhirrelease.md)
  Official releases of the FHIR specification.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: String](hkfhirresource/identifier.md)
  The value from the FHIR resource’s `id` field.
- [var fhirVersion: HKFHIRVersion](hkfhirresource/fhirversion.md)
  The FHIR version used by this resource.
- [var resourceType: HKFHIRResourceType](hkfhirresource/resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [struct HKFHIRResourceType](hkfhirresourcetype.md)
  The FHIR resource types supported in HealthKit.
- [var sourceURL: URL?](hkfhirresource/sourceurl.md)
  The full URL for the source of the FHIR resource.
- [var data: Data](hkfhirresource/data.md)
  The JSON representation of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirversion)*