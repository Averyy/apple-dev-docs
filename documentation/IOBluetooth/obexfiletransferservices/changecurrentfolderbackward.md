# changeCurrentFolderBackward()

**Framework**: IOBluetooth  
**Kind**: method

Change to the directory above the current level if not at the root

**Availability**:
- macOS ?+

## Declaration

```swift
func changeCurrentFolderBackward() -> OBEXError
```

#### Return Value

kOBEXSuccess or kOBEXSessionBusyError initially. Further results returned through the fileTransferServicesPathChangeComplete: delegate method if initially successful.

#### Discussion

Equivalent to ‘cd ..’ only if remote path is not already at root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/changecurrentfolderbackward())*