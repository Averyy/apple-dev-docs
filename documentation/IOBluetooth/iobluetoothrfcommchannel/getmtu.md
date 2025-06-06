# getMTU()

**Framework**: IOBluetooth  
**Kind**: method

Returns the channel maximum transfer unit.

**Availability**:
- macOS ?+

## Declaration

```swift
func getMTU() -> BluetoothRFCOMMMTU
```

#### Return Value

Channel MTU size .

#### Discussion

Returns the length of the largest chunk of data that this channel can carry. If the caller wishes to use the write:length:sleep: api the length of the data can not be bigger than the channel MTU (maximum transfer unit).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/getmtu())*