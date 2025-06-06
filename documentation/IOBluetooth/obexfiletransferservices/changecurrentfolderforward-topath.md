# changeCurrentFolderForward(toPath:)

**Framework**: IOBluetooth  
**Kind**: method

Change the remote path

**Availability**:
- macOS ?+

## Declaration

```swift
func changeCurrentFolderForward(toPath inDirName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesPathChangeComplete: delegate method if initially successful.

#### Discussion

Equivalent to ‘cd dirName’.

## Parameters

- `inDirName`: The name of the remote folder to be set as current


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/changecurrentfolderforward(topath:))*