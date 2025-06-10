# BEExtensionProcess

**Framework**: BrowserEngineKit  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
protocol BEExtensionProcess : NSObjectProtocol
```

## Topics

### Instance Methods
- [func invalidate()](beextensionprocess/invalidate.md)
  Stops the extension process.
- [func makeLibXPCConnectionError() throws -> xpc_connection_t](beextensionprocess/makelibxpcconnectionerror.md)
  Creates a new libXPC connection to the extension process.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess)*