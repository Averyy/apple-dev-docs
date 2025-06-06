# IsSIPProtected

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that tests whether a code file or process is on a volume protected by System Integrity Protection (SIP).

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
struct IsSIPProtected
```

#### Overview

When you use this constraint to test a running process, it tests whether the process’s main executable is SIP-protected.

## Topics

### Initializers
- [init()](issipprotected/init.md)
  Matches if the file is SIP protected.
- [init(Bool)](issipprotected/init(_:).md)
  Matches if the file is or isn’t SIP protected depending on the specified value.
- [init(from: any Decoder) throws](issipprotected/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](issipprotected/encode(to:).md)
  Encodes this value into the given encoder

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
- [struct PlatformType](platformtype.md)
  A constraint that tests whether a code file or running process targets a given platform.
- [struct SigningIdentifier](signingidentifier.md)
  A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/issipprotected)*