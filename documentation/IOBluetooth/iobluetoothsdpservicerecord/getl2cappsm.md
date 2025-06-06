# getL2CAPPSM(_:)

**Framework**: IOBluetooth  
**Kind**: method

Allows the discovery of the L2CAP PSM assigned to the service.

**Availability**:
- macOS ?+

## Declaration

```swift
func getL2CAPPSM(_ outPSM: UnsafeMutablePointer<BluetoothL2CAPPSM>!) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the PSM is found.

#### Discussion

This method will search through the ProtoclDescriptorList attribute to find an entry with the L2CAP UUID (UUID16: 0x0100). If one is found, it gets the second element of the data element sequence and sets the outPSM pointer to it. The PSM value only gets set when kIOReturnSuccess is returned.

## Parameters

- `outPSM`: A pointer to the location that will get the found L2CAP PSM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/getl2cappsm(_:))*