# disconnect()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Disconnect from the remote device

**Availability**:
- macOS

## Declaration

```swift
func disconnect() -> OBEXError
```

```objc
- (OBEXError) disconnect;
```

## Return Value

kOBEXSuccess, kOBEXSessionNotConnectedError, or kOBEXSessionBusyError initially. Further results returned through the fileTransferServicesDisconnectionComplete: delegate method if initially successful.

## Discussion

The user can manually disconnect the OBEXSession from the remote device if they want to. OBEXFileTransferServices will disconnect the OBEXSession at release only if it was responsible for opening the connection via a connect method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/disconnect())*