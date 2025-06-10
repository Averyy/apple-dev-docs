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

### Operators
- [static func == (Mach.PortRightError, Mach.PortRightError) -> Bool](mach/portrighterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Mach.PortRightError.deadName](mach/portrighterror/deadname.md)
  Returned when an operation cannot be completed, because the Mach port right has become a dead name. This is caused by deallocation of the receive right on the other end.
### Instance Properties
- [var hashValue: Int](mach/portrighterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mach/portrighterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mach/portrighterror/equatable-implementations.md)

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