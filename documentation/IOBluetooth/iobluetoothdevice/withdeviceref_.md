# withDeviceRef:

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Type Method

Method call to convert an IOBluetoothDeviceRef into an IOBluetoothDevice *.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
+ (instancetype) withDeviceRef:(IOBluetoothDeviceRef) deviceRef;
```

## Return Value

Returns the IOBluetoothDevice * for the given IOBluetoothDeviceRef.

## Discussion

IOBluetoothDeviceRef and it’s API are deprecated. An IOBluetoothDeviceRef can be cast to a IOBluetoothDevice *

## Parameters

- `deviceRef`: IOBluetoothDeviceRef for which an IOBluetoothDevice * is desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/withdeviceref:)*