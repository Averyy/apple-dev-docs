# copyRemoteFile(_:toLocalPath:)

**Framework**: IOBluetooth  
**Kind**: method

Copy a remote file to a local path

**Availability**:
- macOS ?+

## Declaration

```swift
func copyRemoteFile(_ inRemoteFileName: String!, toLocalPath inLocalPathAndName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError. initially. Further results returned through the fileTransferServicesGetComplete: and fileTransferServicesGetProgress: delegate methods if initially successful.

#### Discussion

Equivalent to ‘cp remotePath/remoteFileName localPathAndName’.

## Parameters

- `inRemoteFileName`: The name of the remote file to get
- `inLocalPathAndName`: The path and name of where the received file will go


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/copyremotefile(_:tolocalpath:))*