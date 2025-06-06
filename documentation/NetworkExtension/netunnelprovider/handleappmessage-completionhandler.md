# handleAppMessage(_:completionHandler:)

**Framework**: Networkextension  
**Kind**: method

Handle messages sent by the tunnel provider extension’s containing app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func handleAppMessage(_ messageData: Data) async -> Data?
```

#### Discussion

Use this method to communicate information between the Tunnel Provider and the Tunnel Provider’s containing app.

> **Note**:  The Tunnel Provider’s containing app may not always be running at the same time as the Tunnel Provider extension. For example, the Tunnel Provider extension may have been started manually from the system’s network settings app or via Connect On Demand. Therefore, you should not rely on this communication channel with the containing app for basic Tunnel Provider operation (start, stop, etc.).

## Parameters

- `messageData`: The message data sent by the tunnel provider extension’s containing app.
- `completionHandler`: A block to be executed by the Tunnel Provider when it is finished handling the message. It may be nil, in which case the containing app does not expect a reply. The provider can send information back to the containing app via the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/handleappmessage(_:completionhandler:))*