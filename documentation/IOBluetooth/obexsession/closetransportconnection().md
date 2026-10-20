# closeTransportConnection()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

You must override this - it will be called when the transport connection should be shutdown.

**Availability**:
- macOS

## Declaration

```swift
func closeTransportConnection() -> OBEXError
```

```objc
- (OBEXError) closeTransportConnection;
```

#### Return Value

Return whether or not the transport connection was closed successfully or not. Return OBEXSuccess ( 0 ) on success, otherwise an error code.

#### Discussion

Tranport subclasses must override this! When called you should take whatever steps are necessary to actually close down the transport connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/closetransportconnection())*