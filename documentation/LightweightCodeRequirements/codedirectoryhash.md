# CodeDirectoryHash

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that matches the hash of a code directory of a code file or of a running or launching process.

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
struct CodeDirectoryHash
```

#### Overview

In the context of [`ProcessCodeRequirement`](processcoderequirement.md) and [`LaunchCodeRequirement`](launchcoderequirement.md) this constraint matches the hash of the chosen code directory for the running process, or the process the system is launching.

In the context of [`OnDiskCodeRequirement`](ondiskcoderequirement.md) this constraint matches the hash of the code directory for the specified `SecStaticCodeRef` that best matches the current architecture. The best match is different for processes running on Intel and Apple silicon, including an Intel process running on Apple silicon with Rosetta. To reliably identify a code file using its code directory hash, use [`in(_:)`](codedirectoryhash/in(_:)-912dv.md) and supply a list of the known code directory hash values.

## Topics

### Initializers
- [init(Data)](codedirectoryhash/init(_:).md)
  Match against a single code directory hash.
- [init(from: any Decoder) throws](codedirectoryhash/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](codedirectoryhash/encode(to:).md)
  Encodes this value into the given encoder
### Type Aliases
- [CodeDirectoryHash.DataType](codedirectoryhash/datatype.md)
  The basic input data type for this constraint: Data
- [CodeDirectoryHash.OutType](codedirectoryhash/outtype.md)
  The type of this constraint: [`CodeDirectoryHash`](codedirectoryhash.md)
### Type Methods
- [static func `in`([CodeDirectoryHash.DataType]) -> CodeDirectoryHash.OutType](codedirectoryhash/in(_:)-1kiuo.md)
  Match against any of the code directory hashes in the provided list.
- [static func `in`(CodeDirectoryHash.DataType...) -> CodeDirectoryHash.OutType](codedirectoryhash/in(_:)-912dv.md)
  Match against any of the code directory hashes in the provided list.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [LaunchConstraint](launchconstraint.md)
- [OnDiskConstraint](ondiskconstraint.md)
- [ProcessConstraint](processconstraint.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [struct PlatformType](platformtype.md)
  A constraint that tests whether a code file or running process targets a given platform.
- [struct SigningIdentifier](signingidentifier.md)
  A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/codedirectoryhash)*