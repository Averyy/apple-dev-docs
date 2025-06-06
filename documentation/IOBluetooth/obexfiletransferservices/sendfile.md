# sendFile(_:)

**Framework**: IOBluetooth  
**Kind**: method

Put a local file to the remote target

**Availability**:
- macOS ?+

## Declaration

```swift
func sendFile(_ inLocalPathAndName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesSendComplete: and fileTransferServicesSendProgress: delegate methods if initially successful.

#### Discussion

Equivalent to ‘mv inLocalFilePath remoteCurrentPath’.

## Parameters

- `inLocalPathAndName`: The name and path of the file to be sent an instance of OBEXFilePut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/sendfile(_:))*