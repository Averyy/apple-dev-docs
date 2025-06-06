# init(discoveredNode:dataReadyHandler:disconnectHandler:)

**Framework**: Core MIDI  
**Kind**: init

Creates a MIDI-CI session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(discoveredNode: MIDICIDiscoveredNode, dataReadyHandler handler: @escaping () -> Void, disconnectHandler: @escaping MIDICISessionDisconnectBlock)
```

## Parameters

- `discoveredNode`: A node found during discovery.
- `handler`: A block the system calls when the session’s data is ready.
- `disconnectHandler`: A block the system calls when you disconnect from the session.

## Topics

### Handling Callbacks
- [typealias MIDICISessionDisconnectBlock](midicisessiondisconnectblock.md)
  A block the system calls when a MIDI-CI session disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/init(discoverednode:datareadyhandler:disconnecthandler:))*