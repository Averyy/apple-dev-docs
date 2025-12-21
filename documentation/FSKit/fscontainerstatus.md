# FSContainerStatus

**Framework**: FSKit  
**Kind**: class

A type that represents a container’s status.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSContainerStatus
```

#### Overview

This type contains two properties:

- The [`state`](fscontainerstatus/state.md) value that indicates the state of the container, such as [`FSContainerState.ready`](fscontainerstate/ready.md) or [`FSContainerState.blocked`](fscontainerstate/blocked.md).
- The [`status`](fscontainerstatus/status.md) is an error (optional in Swift, nullable in Objective-C) that provides further information about the state, such as why the container is blocked.

Examples of statuses that require intervention include errors that indicate the container isn’t ready (POSIX `EAGAIN` or `ENOTCONN`), the container needs authentication (`ENEEDAUTH`), or that authentication failed (`EAUTH`). The status can also be an informative error, such as the FSKit error [`FSError.Code.statusOperationInProgress`](fserror/code/statusoperationinprogress.md).

## Topics

### Creating a container status instance
- [class func active(status: any Error) -> Self](fscontainerstatus/active(status:).md)
  Returns a active container status instance with the provided error status.
- [class func blocked(status: any Error) -> Self](fscontainerstatus/blocked(status:).md)
  Returns a blocked container status instance with the provided error status.
- [class func notReady(status: any Error) -> Self](fscontainerstatus/notready(status:).md)
  Returns a not-ready container status instance with the provided error status.
- [class func ready(status: any Error) -> Self](fscontainerstatus/ready(status:).md)
  Returns a ready container status instance with the provided error status.
### Inspecting status properties
- [var state: FSContainerState](fscontainerstatus/state.md)
  A value that represents the container state, such as ready, active, or blocked.
- [enum FSContainerState](fscontainerstate.md)
  An enumeration of container state values.
- [var status: (any Error)?](fscontainerstatus/status.md)
  An optional error that provides further information about the state.
### Using common status values
- [class var active: FSContainerStatus](fscontainerstatus/active.md)
  A status that represents an active container with no error.
- [class var ready: FSContainerStatus](fscontainerstatus/ready.md)
  A status that represents a ready container with no error.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class FSContainerIdentifier](fscontaineridentifier.md)
  A type that identifies a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus)*