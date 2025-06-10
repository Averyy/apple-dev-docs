# SecCodeStatus

**Framework**: Security  
**Kind**: struct

Operational flags attached by code signing services to running code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecCodeStatus
```

#### Overview

These flags are maintained by the code’s host, and can be read by anyone. Running code may change its own flags, and root may change anyone’s flags. However, each of these flags can change in only one direction and never back, for the lifetime of the code. Not even root can violate this restriction.

All of the bits in the [`SecCodeStatus`](seccodestatus.md) enumeration are reserved by Apple. If you set any bits not defined here, the behavior is undefined.

## Topics

### Initializers
- [init(rawValue: UInt32)](seccodestatus/init(rawvalue:).md)
### Constants
- [static var valid: SecCodeStatus](seccodestatus/valid.md)
  The code is dynamically valid.
- [static var hard: SecCodeStatus](seccodestatus/hard.md)
  The code prefers to be denied access to resources if gaining access would invalidate it.
- [static var kill: SecCodeStatus](seccodestatus/kill.md)
  The code wants to be terminated if it ever loses its validity.
- [static var debugged: SecCodeStatus](seccodestatus/debugged.md)
  The code has been debugged by another process that was allowed to do so.
- [static var platform: SecCodeStatus](seccodestatus/platform.md)
  The code ships with the operating system and is signed by Apple.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodestatus)*