# removeItem(_:)

**Framework**: IOBluetooth  
**Kind**: method

Remove a remote item.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeItem(_ inItemName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesRemoveItemComplete: delegate method if initially successful.

#### Discussion

Not supported for use on Apple computer targets

## Parameters

- `inItemName`: The name of the remote item to be removed


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/removeitem(_:))*