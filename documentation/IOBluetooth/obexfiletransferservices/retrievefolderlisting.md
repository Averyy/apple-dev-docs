# retrieveFolderListing()

**Framework**: IOBluetooth  
**Kind**: method

Get a remote directory listing

**Availability**:
- macOS ?+

## Declaration

```swift
func retrieveFolderListing() -> OBEXError
```

#### Return Value

kOBEXSuccess or kOBEXSessionBusyError initially. Further results returned through the fileTransferServicesRetrieveFolderListingComplete: delegate method if initially successful.

#### Discussion

Equivalent to ‘ls’.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/retrievefolderlisting())*