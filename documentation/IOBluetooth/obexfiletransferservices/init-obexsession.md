# init(obexSession:)

**Framework**: IOBluetooth  
**Kind**: init

Create a new OBEXFileTransferServices object

**Availability**:
- macOS ?+

## Declaration

```swift
init!(obexSession inOBEXSession: IOBluetoothOBEXSession!)
```

#### Return Value

A newly created OBEXFileTransferServices object on success, nil on failure

#### Discussion

This object must be constructed with a valid IOBluetoothOBEXSession. The given IOBluetoothOBEXSession does not need to be connected to the remote server. OBEXFileTransferServices can be manually connected through the provided connection methods.

## Parameters

- `inOBEXSession`: A valid IOBluetoothOBEXSession


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/init(obexsession:))*