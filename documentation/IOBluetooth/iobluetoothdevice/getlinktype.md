# getLinkType()

**Framework**: IOBluetooth  
**Kind**: method

Get the link type for the baseband connection.

**Availability**:
- macOS ?+

## Declaration

```swift
func getLinkType() -> BluetoothLinkType
```

#### Return Value

Returns the link type for the baseband connection. If no baseband connection is present, kBluetoothLinkTypeNone is returned.

#### Discussion

This method only returns a valid result if a baseband connection is present (-isConnected returns TRUE).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getlinktype())*