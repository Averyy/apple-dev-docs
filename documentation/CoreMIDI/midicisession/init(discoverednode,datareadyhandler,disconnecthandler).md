# init(discoveredNode:dataReadyHandler:disconnectHandler:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a MIDI-CI session.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
init(discoveredNode: MIDICIDiscoveredNode, dataReadyHandler handler: @escaping () -> Void, disconnectHandler: @escaping MIDICISessionDisconnectBlock)
```

```objc
- (instancetype) initWithDiscoveredNode:(MIDICIDiscoveredNode *) discoveredNode dataReadyHandler:(void (^)()) handler disconnectHandler:(MIDICISessionDisconnectBlock) disconnectHandler;
```

## Parameters

- `discoveredNode`: A node found during discovery.
- `handler`: A block the system calls when the session’s data is ready.
- `disconnectHandler`: A block the system calls when you disconnect from the session.

## Topics

### Handling Callbacks
- [typealias MIDICISessionDisconnectBlock](../midicisessiondisconnectblock.md)
  A block the system calls when a MIDI-CI session disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/init(discoverednode:datareadyhandler:disconnecthandler:))*