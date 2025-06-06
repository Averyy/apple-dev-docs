# closeTransportConnection()

**Framework**: IOBluetooth  
**Kind**: method

You must override this - it will be called when the transport connection should be shutdown.

**Availability**:
- macOS ?+

## Declaration

```swift
func closeTransportConnection() -> OBEXError
```

#### Return Value

Return whether or not the transport connection was closed successfully or not. Return OBEXSuccess ( 0 ) on success, otherwise an error code.

#### Discussion

Tranport subclasses must override this! When called you should take whatever steps are necessary to actually close down the transport connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/closetransportconnection())*