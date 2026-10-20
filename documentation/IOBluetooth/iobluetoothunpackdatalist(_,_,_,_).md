# IOBluetoothUnpackDataList(_:_:_:_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothUnpackDataList(_ inBufferSize: Int, _ inBuffer: UnsafeRawPointer!, _ inFormat: UnsafePointer<CChar>!, _ inArgs: CVaListPointer) -> Int
```

```c
extern long IOBluetoothUnpackDataList(ByteCount inBufferSize, const void *inBuffer, const char *inFormat, va_list inArgs);
```

## See Also

### Functions
- [func IOBluetoothNSStringFromDeviceAddressColon(UnsafePointer<BluetoothDeviceAddress>!) -> String!](./iobluetoothnsstringfromdeviceaddresscolon%28_%29.md)
- [func IOBluetoothPackDataList(UnsafeMutableRawPointer!, UnsafePointer<CChar>!, CVaListPointer) -> Int](./iobluetoothpackdatalist%28_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothunpackdatalist(_:_:_:_:))*