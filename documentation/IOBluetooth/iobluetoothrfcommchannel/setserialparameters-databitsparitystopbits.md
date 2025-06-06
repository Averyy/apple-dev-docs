# setSerialParameters(_:dataBits:parity:stopBits:)

**Framework**: IOBluetooth  
**Kind**: method

Changes the parameters of the serial connection.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSerialParameters(_ speed: UInt32, dataBits nBits: UInt8, parity: BluetoothRFCOMMParityType, stopBits bitStop: UInt8) -> IOReturn
```

#### Return Value

An error code value. 0 if successful.

## Parameters

- `speed`: The baudrate.
- `nBits`: Number of data bits.
- `parity`: The type of parity can be NoParity, OddParity, EvenParity or MaxParity.
- `bitStop`: Number of stop bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/setserialparameters(_:databits:parity:stopbits:))*