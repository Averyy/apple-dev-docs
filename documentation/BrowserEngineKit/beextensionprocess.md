# BEExtensionProcess

**Framework**: BrowserEngineKit  
**Kind**: protocol

A common protocol that creates XPC connections for an extension process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
protocol BEExtensionProcess : NSObjectProtocol
```

#### Overview

This protocol is common across extension processes for networking ([`BENetworkingProcess`](benetworkingprocess.md)), rendering ([`BERenderingProcess`](berenderingprocess.md)), and web content ([`BEWebContentProcess`](bewebcontentprocess.md)).

Create an XPC connection for an extension process with the [`makeLibXPCConnectionError()`](beextensionprocess/makelibxpcconnectionerror().md) method. Stop an extension process with [`invalidate()`](beextensionprocess/invalidate().md).

## Topics

- [func invalidate()](beextensionprocess/invalidate.md)
  Stops the extension process.
- [func makeLibXPCConnectionError() throws -> xpc_connection_t](beextensionprocess/makelibxpcconnectionerror.md)
  Creates a new libXPC connection to the extension process.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)
  Coordinate helper processes to efficiently support your browser app.
- [Using XPC to communicate with browser extensions](using-xpc-to-communicate-with-browser-extensions.md)
  Build interprocess communication between your host app and extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess)*