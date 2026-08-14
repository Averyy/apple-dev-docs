# SessionCreationFlags

**Framework**: Security  
**Kind**: struct

The flags that affect the creation of a security session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SessionCreationFlags
```

## Topics

### Initializers
- [init(rawValue: UInt32)](sessioncreationflags/init(rawvalue:).md)
  Initializes a session creation flags value.
### Flags
- [static var sessionKeepCurrentBootstrap: SessionCreationFlags](sessioncreationflags/sessionkeepcurrentbootstrap.md)
  The caller has allocated sub-bootstrap.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessioncreationflags)*