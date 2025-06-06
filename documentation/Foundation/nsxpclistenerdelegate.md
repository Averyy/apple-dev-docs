# NSXPCListenerDelegate

**Framework**: Foundation  
**Kind**: protocol

The protocol that delegates to the XPC listener use to accept or reject new connections.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSXPCListenerDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func listener(NSXPCListener, shouldAcceptNewConnection: NSXPCConnection) -> Bool](nsxpclistenerdelegate/listener(_:shouldacceptnewconnection:).md)
  Accepts or rejects a new connection to the listener.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSXPCListener](nsxpclistener.md)
  A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [class NSXPCListenerEndpoint](nsxpclistenerendpoint.md)
  An object that names a specific XPC listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate)*