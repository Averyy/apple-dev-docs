# subscriberNumber()

**Framework**: IOBluetooth  
**Kind**: method

Requests that the Bluetooth audio gateway send the subscriber number to the delegate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func subscriberNumber()
```

#### Discussion

The subscriber number is sent to the [`handsFree(_:subscriberNumber:)`](iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:).md) function of the delegate.

## See Also

- [func currentCallList()](iobluetoothhandsfreedevice/currentcalllist.md)
  Requests that the Bluetooth audio gateway send the delegate a list of calls that are active, on hold, or being set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/subscribernumber())*