# connectToFTPService()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Connect to a remote device for FTP operations

**Availability**:
- macOS

## Declaration

```swift
func connectToFTPService() -> OBEXError
```

```objc
- (OBEXError) connectToFTPService;
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXSessionAlreadyConnectedError, kOBEXNoResourcesError initially. Further results returned through the fileTransferServicesConnectionComplete: delegate method if initially successful.

#### Discussion

If the OBEXSession given to OBEXFileTransferServices on creation is not connected it can be manually connected through this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/connecttoftpservice())*