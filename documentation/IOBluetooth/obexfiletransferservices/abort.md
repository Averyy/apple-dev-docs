# abort()

**Framework**: IOBluetooth  
**Kind**: method

Abort the current operation

**Availability**:
- macOS ?+

## Declaration

```swift
func abort() -> OBEXError
```

#### Return Value

kOBEXSuccess, or kOBEXGeneralError if no command is in progress. ABORT commands can only be sent on our turn, meaning we may have to timeout if the target side never responds to the command in progress. In that case this object will call back with a status of kOBEXTimeoutError and an error. Further results returned through the fileTransferServicesAbortComplete: delegate method if initially successful.

#### Discussion

Attempts send an abort request to the remote device. Returns the OBEXFileTransferServices object to an idle state though the state of the remote device is not guaranteed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/abort())*