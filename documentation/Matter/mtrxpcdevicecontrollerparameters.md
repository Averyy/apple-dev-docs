# MTRXPCDeviceControllerParameters

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
class MTRXPCDeviceControllerParameters
```

## Topics

### Initializers
- [init(XPCConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](mtrxpcdevicecontrollerparameters/init(xpcconnectionblock:uniqueidentifier:)-3wkoh.md)
- [init(XPConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](mtrxpcdevicecontrollerparameters/init(xpconnectionblock:uniqueidentifier:)-5vgjx.md)
- [init(xpConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](mtrxpcdevicecontrollerparameters/init(xpconnectionblock:uniqueidentifier:)-44d5q.md)
- [init(xpcConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](mtrxpcdevicecontrollerparameters/init(xpcconnectionblock:uniqueidentifier:)-9ep5u.md)
  A controller created from this way will connect to a remote instance of an MTRDeviceController loaded in an XPC Service
### Instance Properties
- [var uniqueIdentifier: UUID](mtrxpcdevicecontrollerparameters/uniqueidentifier.md)
- [var xpcConnectionBlock: () -> NSXPCConnection](mtrxpcdevicecontrollerparameters/xpcconnectionblock.md)

## Relationships

### Inherits From
- [MTRDeviceControllerAbstractParameters](mtrdevicecontrollerabstractparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters)*