# currentCallList()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Requests that the Bluetooth audio gateway send the delegate a list of calls that are active, on hold, or being set up.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func currentCallList()
```

```objc
- (void) currentCallList;
```

#### Discussion

The [`handsFree(_:currentCall:)`](../iobluetoothhandsfreedevicedelegate/handsfree%28_,currentcall%29.md) function of the delegate is called once for each current call.

## See Also

### Requesting Status Information
- [func subscriberNumber()](./subscribernumber%28%29.md)
  Requests that the Bluetooth audio gateway send the subscriber number to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/currentcalllist())*