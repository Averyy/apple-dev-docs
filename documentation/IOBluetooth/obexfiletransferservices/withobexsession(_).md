# withOBEXSession(_:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Type Method

Create a new OBEXFileTransferServices object

**Availability**:
- macOS

## Declaration

```swift
class func withOBEXSession(_ inOBEXSession: IOBluetoothOBEXSession!) -> Self!
```

```objc
+ (instancetype) withOBEXSession:(IOBluetoothOBEXSession *) inOBEXSession;
```

## Return Value

A newly created OBEXFileTransferServices object on success, nil on failure

## Discussion

This object must be constructed with a valid IOBluetoothOBEXSession. The given IOBluetoothOBEXSession does not need to be connected to the remote server. This module can be manually connected through the connect() method.

## Parameters

- `inOBEXSession`: A valid IOBluetoothOBEXSession


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/withobexsession(_:))*