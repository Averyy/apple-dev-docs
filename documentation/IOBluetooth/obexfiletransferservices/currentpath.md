# currentPath()

**Framework**: IOBluetooth  
**Kind**: method

Get the remote current directory path during an FTP session

**Availability**:
- macOS ?+

## Declaration

```swift
func currentPath() -> String!
```

#### Return Value

The current path being browsed over FTP

#### Discussion

This path is changed with each path-specific command called on OBEXFileTransferServices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/currentpath())*