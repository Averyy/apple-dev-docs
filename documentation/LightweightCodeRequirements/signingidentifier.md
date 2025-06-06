# SigningIdentifier

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that tests whether the provided signing identifier matches the signature attached to the code.

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
struct SigningIdentifier
```

#### Overview

The signing identifier is referred to as simply the “Identifier” in codesign –dump output. The signing identifier is matched byte for byte (i.e. no unicode normalization occurs). Signing identifiers can be claimed by multiple signers. To check a signing identifier securely you should also require a [`ValidationCategory`](validationcategory.md) constraint and for non-Apple code a [`TeamIdentifier`](teamidentifier.md) constraint.

## Topics

### Initializers
- [init(String)](signingidentifier/init(_:).md)
  Matches if the provided string matches the signing identifier of the code.
- [init(from: any Decoder) throws](signingidentifier/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](signingidentifier/encode(to:).md)
  Encodes this value into the given encoder
### Type Aliases
- [SigningIdentifier.DataType](signingidentifier/datatype.md)
  The basic input data type for this constraint: String.
- [SigningIdentifier.OutType](signingidentifier/outtype.md)
  The type of this constraint: [`SigningIdentifier`](signingidentifier.md).
### Type Methods
- [static func `in`(SigningIdentifier.DataType...) -> SigningIdentifier.OutType](signingidentifier/in(_:)-57h8m.md)
  Matches if the signing identifier of the code matches any of the provided signing identifiers.
- [static func `in`([SigningIdentifier.DataType]) -> SigningIdentifier.OutType](signingidentifier/in(_:)-57qq8.md)
  Matches if the signing identifier of the code matches any of the provided signing identifiers.

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
- [struct PlatformType](platformtype.md)
  A constraint that tests whether a code file or running process targets a given platform.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/signingidentifier)*