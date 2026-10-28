# IOBluetoothHandsFreeCallStatus

**Framework**: IOBluetooth  
**Kind**: var  
**Role**: Global Variable

The current state of the call.

**Availability**:
- macOS

## Declaration

```swift
let IOBluetoothHandsFreeCallStatus: String
```

```c
extern NSString * const IOBluetoothHandsFreeCallStatus;
```

## Discussion

The string contains a single digit with one of the following values:

- **`“0”`**: An active call.
- **`“1”`**: An active call that’s on hold.
- **`“2”`**: An outgoing call that’s dialing.
- **`“3”`**: An outgoing call that’s alerting the receiver.
- **`“4”`**: An incoming call.
- **`“5”`**: A call that’s waiting.

## See Also

### Call Information
- [let IOBluetoothHandsFreeCallDirection: String](./iobluetoothhandsfreecalldirection.md)
  A value that indicates whether a call is incoming or outgoing.
- [let IOBluetoothHandsFreeCallIndex: String](./iobluetoothhandsfreecallindex.md)
  The index of the call, starting with `1`.
- [let IOBluetoothHandsFreeCallMode: String](./iobluetoothhandsfreecallmode.md)
  The type of call data.
- [let IOBluetoothHandsFreeCallMultiparty: String](./iobluetoothhandsfreecallmultiparty.md)
  A value that indicates whether the call is multiple-party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallstatus)*