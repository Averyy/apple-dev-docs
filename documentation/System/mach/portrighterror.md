# Mach.PortRightError

**Framework**: System  
**Kind**: enum

Possible errors that can be thrown by Mach.Port operations.

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
enum PortRightError
```

## Topics

### Enumeration Cases
- [Mach.PortRightError.deadName](mach/portrighterror/deadname.md)
  Returned when an operation cannot be completed, because the Mach port right has become a dead name. This is caused by deallocation of the receive right on the other end.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/portrighterror)*