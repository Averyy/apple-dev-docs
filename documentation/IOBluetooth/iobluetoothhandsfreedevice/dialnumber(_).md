# dialNumber(_:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Calls the phone number on a hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func dialNumber(_ aNumber: String!)
```

```objc
- (void) dialNumber:(NSString *) aNumber;
```

## Parameters

- `aNumber`: A string containing a phone number.

## See Also

### Dialing Calls
- [func memoryDial(Int32)](./memorydial%28_%29.md)
  Calls the phone number stored in a speed dial or memory slot of the hands-free phone or headset.
- [func redial()](./redial%28%29.md)
  Calls the number stored on the hands-free phone or headset again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/dialnumber(_:))*