# IOBluetoothHandsFreeCallIndex

**Framework**: IOBluetooth  
**Kind**: var  
**Role**: Global Variable

The index of the call, starting with `1`.

**Availability**:
- macOS

## Declaration

```swift
let IOBluetoothHandsFreeCallIndex: String
```

```c
extern NSString * const IOBluetoothHandsFreeCallIndex;
```

#### Discussion

Calls keep their index number until they are ended. New calls are assigned the lowest available index number.

## See Also

### Call Information
- [let IOBluetoothHandsFreeCallDirection: String](./iobluetoothhandsfreecalldirection.md)
  A value that indicates whether a call is incoming or outgoing.
- [let IOBluetoothHandsFreeCallMode: String](./iobluetoothhandsfreecallmode.md)
  The type of call data.
- [let IOBluetoothHandsFreeCallMultiparty: String](./iobluetoothhandsfreecallmultiparty.md)
  A value that indicates whether the call is multiple-party.
- [let IOBluetoothHandsFreeCallStatus: String](./iobluetoothhandsfreecallstatus.md)
  The current state of the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecallindex)*