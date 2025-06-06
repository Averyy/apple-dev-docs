# PlatformType

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that tests whether a code file or running process targets a given platform.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct PlatformType
```

#### Overview

For [`ProcessCodeRequirement`](processcoderequirement.md) and [`LaunchCodeRequirement`](launchcoderequirement.md) this constraint matches the platform type of the process  as known to the kernel. For [`OnDiskCodeRequirement`](ondiskcoderequirement.md) this constraint matches the platforms supported in Mach-O load commands. The [`OnDiskCodeRequirement`](ondiskcoderequirement.md) will be matched against a SecStaticCodeRef. For this constraint to match, the SecStaticCodeRef must reference a Mach-O. If the SecStaticCodeRef references a specific architecture of a Mach-O then this constraint will be matched against the first LC_BUILD_VERSION or LC_VERSION_MIN_*OS load command in the Mach-O. If the SecStaticCodeRef references a file, then this constraint will match against the load commands in the architecture that is most likely to run on the platform the code is running on.

## Topics

### Structures
- [PlatformType.Value](platformtype/value.md)
  Supported Platform Types for a process
### Initializers
- [init(PlatformType.Value)](platformtype/init(_:).md)
  Matches if the process is running as the specified platform type or if the file supports the specified platform type.
- [init(from: any Decoder) throws](platformtype/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](platformtype/encode(to:).md)
  Encodes this value into the given encoder
### Type Aliases
- [PlatformType.DataType](platformtype/datatype.md)
  The basic input data type of this constraint: `PlatformType.Value`..
- [PlatformType.OutType](platformtype/outtype.md)
  The type of this constraint: [`PlatformType`](platformtype.md)
### Type Methods
- [static func `in`(PlatformType.DataType...) -> PlatformType.OutType](platformtype/in(_:)-1ndmu.md)
  Matches if the process is running as any of the specified platform types or if the file supports any of the specified platform types.
- [static func `in`([PlatformType.DataType]) -> PlatformType.OutType](platformtype/in(_:)-44pc3.md)
  Matches if the process is running as any of the specified platform types or if the file supports any of the specified platform types.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [LaunchConstraint](launchconstraint.md)
- [OnDiskConstraint](ondiskconstraint.md)
- [ProcessConstraint](processconstraint.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CodeDirectoryHash](codedirectoryhash.md)
  A constraint that matches the hash of a code directory of a code file or of a running or launching process.
- [class EntitlementsQuery](entitlementsquery.md)
  A constraint that tests values in the entitlements dictionary associated with a process or code file.
- [struct InfoPlistHash](infoplisthash.md)
  A constraint that tests the specified hash against the Information property list hash stored in the code signature of the process or code file.
- [struct IsInitProcess](isinitprocess.md)
  A constraint that tests whether a process is the operating system’s initial process.
- [struct IsMainBinary](ismainbinary.md)
  A constraint that tests whether a code file is a main binary.
- [struct IsSIPProtected](issipprotected.md)
  A constraint that tests whether a code file or process is on a volume protected by System Integrity Protection (SIP).
- [struct SigningIdentifier](signingidentifier.md)
  A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype)*