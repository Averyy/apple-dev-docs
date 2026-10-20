# FSContainerIdentifier

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A type that identifies a container.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSContainerIdentifier
```

```objc
@interface FSContainerIdentifier : FSEntityIdentifier
```

#### Overview

The identifier is either a UUID or a UUID with additional differentiating bytes. Some network protocols evaluate access based on a user ID when connecting. In this situation, when a file server receives multiple client connections with different user IDs, the server provides different file hierarchies to each. For such systems, represent the container identifier as the UUID associated with the server, followed by four or eight bytes to differentiate connections.

> ❗ **Important**: Don’t subclass this class.

## Topics

### Accessing identifier properties
- [var volumeIdentifier: FSVolume.Identifier](./fscontaineridentifier/volumeidentifier.md)
  The volume identifier associated with the container.

## Relationships

### Inherits From
- [FSEntityIdentifier](./fsentityidentifier.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Containers
- [class FSContainerStatus](./fscontainerstatus.md)
  A type that represents a container’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontaineridentifier)*