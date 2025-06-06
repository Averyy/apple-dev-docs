# getDefaultVCard(_:)

**Framework**: IOBluetooth  
**Kind**: method

Get the remote default VCard, if it is supported

**Availability**:
- macOS ?+

## Declaration

```swift
func getDefaultVCard(_ inLocalPathAndName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesGetComplete: and fileTransferServicesGetProgress: delegate methods if initially successful.

#### Discussion

Some devices such as cellphones and computers support default VCards

## Parameters

- `inLocalPathAndName`: The path and name of where the received file will go


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/getdefaultvcard(_:))*