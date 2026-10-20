# MTRXPCDeviceControllerParameters

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRXPCDeviceControllerParameters : MTRDeviceControllerAbstractParameters
```

## Topics

### Initializers
- [init(XPCConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](./mtrxpcdevicecontrollerparameters/init%28xpcconnectionblock,uniqueidentifier%29-3wkoh.md)
- [init(XPConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](./mtrxpcdevicecontrollerparameters/init%28xpconnectionblock,uniqueidentifier%29-5vgjx.md)
- [init(xpConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](./mtrxpcdevicecontrollerparameters/init%28xpconnectionblock,uniqueidentifier%29-44d5q.md)
- [init(xpcConnectionBlock: () -> NSXPCConnection, uniqueIdentifier: UUID)](./mtrxpcdevicecontrollerparameters/init%28xpcconnectionblock,uniqueidentifier%29-9ep5u.md)
  A controller created from this way will connect to a remote instance of an MTRDeviceController loaded in an XPC Service
### Instance Properties
- [var uniqueIdentifier: UUID](./mtrxpcdevicecontrollerparameters/uniqueidentifier.md)
- [var xpcConnectionBlock: () -> NSXPCConnection](./mtrxpcdevicecontrollerparameters/xpcconnectionblock.md)

## Relationships

### Inherits From
- [MTRDeviceControllerAbstractParameters](./mtrdevicecontrollerabstractparameters.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters)*