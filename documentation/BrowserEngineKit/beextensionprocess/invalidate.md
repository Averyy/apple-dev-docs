# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Stops the extension process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

Call this method to signal to the system your app no longer needs the extension process. If this is the last connection from the system to the extension, the system ends the extension process.

## See Also

- [func makeLibXPCConnectionError() throws -> xpc_connection_t](beextensionprocess/makelibxpcconnectionerror.md)
  Creates a new libXPC connection to the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess/invalidate())*