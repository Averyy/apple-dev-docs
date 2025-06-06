# Mach

**Framework**: System  
**Kind**: enum

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
@frozen
enum Mach
```

## Topics

### Structures
- [struct Port](mach/port.md)
- [struct ReceiveRight](mach/receiveright.md)
  The MachPortRight type used to manage a receive right.
- [struct SendOnceRight](mach/sendonceright.md)
  The MachPortRight type used to manage a send-once right.
- [struct SendRight](mach/sendright.md)
  The MachPortRight type used to manage a send right.
### Enumerations
- [Mach.PortRightError](mach/portrighterror.md)
  Possible errors that can be thrown by Mach.Port operations.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach)*