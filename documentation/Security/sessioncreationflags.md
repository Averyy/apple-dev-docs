# SessionCreationFlags

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

The flags that affect the creation of a security session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SessionCreationFlags
```

```c
enum SessionCreationFlags : UInt32;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./sessioncreationflags/init%28rawvalue%29.md)
  Initializes a session creation flags value.
### Flags
- [static var sessionKeepCurrentBootstrap: SessionCreationFlags](./sessioncreationflags/sessionkeepcurrentbootstrap.md)
  The caller has allocated sub-bootstrap.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessioncreationflags)*