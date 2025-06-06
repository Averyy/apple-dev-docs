# currentCallList()

**Framework**: IOBluetooth  
**Kind**: method

Requests that the Bluetooth audio gateway send the delegate a list of calls that are active, on hold, or being set up.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func currentCallList()
```

#### Discussion

The [`handsFree(_:currentCall:)`](iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:).md) function of the delegate is called once for each current call.

## See Also

- [func subscriberNumber()](iobluetoothhandsfreedevice/subscribernumber.md)
  Requests that the Bluetooth audio gateway send the subscriber number to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/currentcalllist())*