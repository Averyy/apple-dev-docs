# getEncryptionMode()

**Framework**: IOBluetooth  
**Kind**: method

Get the encryption mode for the baseband connection.

**Availability**:
- macOS ?+

## Declaration

```swift
func getEncryptionMode() -> BluetoothHCIEncryptionMode
```

#### Return Value

Returns the encryption mode for the baseband connection. If no baseband connection is present, kEncryptionDisabled is returned.

#### Discussion

This method only returns a valid result if a baseband connection is present (-isConnected returns TRUE).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getencryptionmode())*