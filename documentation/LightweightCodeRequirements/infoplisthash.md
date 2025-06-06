# InfoPlistHash

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that tests the specified hash against the Information property list hash stored in the code signature of the process or code file.

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
struct InfoPlistHash
```

## Topics

### Initializers
- [init(Data)](infoplisthash/init(_:).md)
  Match against a single Info.plist hash
- [init(from: any Decoder) throws](infoplisthash/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](infoplisthash/encode(to:).md)
  Encodes this value into the given encoder
### Type Aliases
- [InfoPlistHash.DataType](infoplisthash/datatype.md)
- [InfoPlistHash.OutType](infoplisthash/outtype.md)
  The type of this constraint: [`InfoPlistHash`](infoplisthash.md).
### Type Methods
- [static func `in`(InfoPlistHash.DataType...) -> InfoPlistHash.OutType](infoplisthash/in(_:)-18amo.md)
  Match against any of the Info.plist hashes in the provided list.
- [static func `in`([InfoPlistHash.DataType]) -> InfoPlistHash.OutType](infoplisthash/in(_:)-1rwy8.md)
  Match against any of the Info.plist hashes in the provided list.

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

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/infoplisthash)*