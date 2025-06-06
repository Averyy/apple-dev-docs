# FSContainerIdentifier

**Framework**: FSKit  
**Kind**: class

A type that identifies a container.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSContainerIdentifier
```

#### Overview

The identifier is either a UUID or a UUID with additional differentiating bytes. Some network protocols evaluate access based on a user ID when connecting. In this situation, when a file server receives multiple client connections with different user IDs, the server provides different file hierarchies to each. For such systems, represent the container identifier as the UUID associated with the server, followed by four or eight bytes to differentiate connections.

> ❗ **Important**: Don’t subclass this class.

Don’t subclass this class.

## Topics

### Accessing identifier properties
- [var volumeIdentifier: FSVolume.Identifier](fscontaineridentifier/volumeidentifier.md)
  The volume identifier associated with the container.

## Relationships

### Inherits From
- [FSEntityIdentifier](fsentityidentifier.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class FSContainerStatus](fscontainerstatus.md)
  A type that represents a container’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontaineridentifier)*