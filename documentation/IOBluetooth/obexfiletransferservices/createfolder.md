# createFolder(_:)

**Framework**: IOBluetooth  
**Kind**: method

Create a folder on the remote target

**Availability**:
- macOS ?+

## Declaration

```swift
func createFolder(_ inDirName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesCreateFolderComplete delegate method if initially successful.

#### Discussion

Equivalent to ‘mkdir dirName’.

## Parameters

- `inDirName`: The name of the folder to be created


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/createfolder(_:))*