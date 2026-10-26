---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocksemanticversion"
framework: "CareKit/CareKitStore"
---

# OCKSemanticVersion

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A semantic version with major, minor, and patch version numbers. Semantic versions parsed from strings and compared.

## Declaration

```swift
struct OCKSemanticVersion
```

## Topics

### Operators
- [static func < (OCKSemanticVersion, OCKSemanticVersion) -> Bool](./ocksemanticversion/op%28_,_%29.md)
### Initializers
- [init?(String)](./ocksemanticversion/init%28_%29.md)
  Initialize from a string description of the semantic version. This init will fail and return nil if the provided string is not a valid semantic version.
- [init(from: any Decoder) throws](./ocksemanticversion/init%28from%29.md)
- [init(majorVersion: Int, minorVersion: Int, patchNumber: Int)](./ocksemanticversion/init%28majorversion,minorversion,patchnumber%29.md)
  Initialize by specifying the major, minor, and patch versions.
### Instance Properties
- [var description: String](./ocksemanticversion/description.md)
- [let majorVersion: Int](./ocksemanticversion/majorversion.md)
  The major version number, i.e. the *3* in 3.11.2.
- [let minorVersion: Int](./ocksemanticversion/minorversion.md)
  The minor version number, i.e. the *11* in 3.11.2.
- [let patchNumber: Int](./ocksemanticversion/patchnumber.md)
  The patch number, i.e. the *2* in 3.11.2.
### Type Methods
- [static func parse(String) throws -> OCKSemanticVersion](./ocksemanticversion/parse%28_%29.md)
  Parses a string into an `OCKSemanticVersion`. Throws if an error occurs.
### Enumerations
- [OCKSemanticVersion.ParsingError](./ocksemanticversion/parsingerror.md)
  The errors that could occur while attempting to parse a string into an `OCKSemanticVersion`.
### Default Implementations
- [Comparable Implementations](./ocksemanticversion/comparable-implementations.md)
- [Equatable Implementations](./ocksemanticversion/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Comparable
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.LosslessStringConvertible
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocksemanticversion)*