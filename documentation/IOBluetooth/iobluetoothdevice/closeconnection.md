# closeConnection()

**Framework**: IOBluetooth  
**Kind**: method

Close down the baseband connection to the device.

**Availability**:
- macOS ?+

## Declaration

```swift
func closeConnection() -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the connection has successfully been closed.

#### Discussion

This method is synchronous and will not return until the connection has been closed (or the command failed). In the future this API will be changed to allow asynchronous operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/closeconnection())*