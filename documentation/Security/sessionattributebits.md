# SessionAttributeBits

**Framework**: Security  
**Kind**: struct

The attributes of a security session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SessionAttributeBits
```

## Topics

### Initializers
- [init(rawValue: UInt32)](sessionattributebits/init(rawvalue:).md)
  Initializes a session attribute bits structure.
### Bits
- [static var sessionIsRoot: SessionAttributeBits](sessionattributebits/sessionisroot.md)
  A bit that indicates the session is the root session.
- [static var sessionHasGraphicAccess: SessionAttributeBits](sessionattributebits/sessionhasgraphicaccess.md)
  A bit that indicates a graphic subsystem is available.
- [static var sessionHasTTY: SessionAttributeBits](sessionattributebits/sessionhastty.md)
  A bit that indicates `/dev/tty` is available.
- [static var sessionIsRemote: SessionAttributeBits](sessionattributebits/sessionisremote.md)
  A bit that indicates the session was initiated over the network.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessionattributebits)*