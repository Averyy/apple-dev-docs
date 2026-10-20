# makeLibXPCConnectionError()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new libXPC connection to the extension process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
func makeLibXPCConnectionError() throws -> xpc_connection_t
```

```objc
- (xpc_connection_t) makeLibXPCConnectionError:(NSError **) error;
```

#### Return Value

The connection object representing the created libXPC connection or `nil`.

#### Discussion

This method creates a connection to the extension process and returns it. If it isn’t possible to make an XPC connection, this method returns `nil` and populates the `error` parameter.

## See Also

- [func invalidate()](./invalidate%28%29.md)
  Stops the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess/makelibxpcconnectionerror())*