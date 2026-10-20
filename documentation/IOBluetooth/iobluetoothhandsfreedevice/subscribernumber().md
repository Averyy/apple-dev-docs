# subscriberNumber()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Requests that the Bluetooth audio gateway send the subscriber number to the delegate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func subscriberNumber()
```

```objc
- (void) subscriberNumber;
```

#### Discussion

The subscriber number is sent to the [`handsFree(_:subscriberNumber:)`](../iobluetoothhandsfreedevicedelegate/handsfree%28_,subscribernumber%29.md) function of the delegate.

## See Also

### Requesting Status Information
- [func currentCallList()](./currentcalllist%28%29.md)
  Requests that the Bluetooth audio gateway send the delegate a list of calls that are active, on hold, or being set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/subscribernumber())*