# IOUSBHostCIMessageStatusToIOReturn(_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBHostCIMessageStatusToIOReturn(_ status: IOUSBHostCIMessageStatus) -> IOReturn
```

```c
IOReturn IOUSBHostCIMessageStatusToIOReturn(IOUSBHostCIMessageStatus status);
```

## See Also

### Functions
- [func IOUSBGetEndpointBurstSize(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!, UnsafePointer<IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor>!) -> UInt32](./iousbgetendpointburstsize%28_,_,_,_%29.md)
- [func IOUSBGetEndpointMult(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!, UnsafePointer<IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor>!) -> UInt8](./iousbgetendpointmult%28_,_,_,_%29.md)
- [func IOUSBGetEndpointSynchronizationType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointsynchronizationtype%28_%29.md)
- [func IOUSBGetEndpointUsageType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointusagetype%28_%29.md)
- [func IOUSBGetPlatformCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBPlatformCapabilityDescriptor>!](./iousbgetplatformcapabilitydescriptor%28_%29.md)
- [func IOUSBGetPlatformCapabilityDescriptorWithUUID(UnsafePointer<IOUSBBOSDescriptor>!, UnsafeMutablePointer<UInt8>!) -> UnsafePointer<IOUSBPlatformCapabilityDescriptor>!](./iousbgetplatformcapabilitydescriptorwithuuid%28_,_%29.md)
- [func IOUSBGetSuperSpeedPlusDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedPlusUSB>!](./iousbgetsuperspeedplusdevicecapabilitydescriptor%28_%29.md)
- [func IOUSBHostCIControllerStateToString(IOUSBHostCIControllerState) -> UnsafePointer<CChar>!](./iousbhostcicontrollerstatetostring%28_%29.md)
- [func IOUSBHostCIDeviceSpeedToString(IOUSBHostCIDeviceSpeed) -> UnsafePointer<CChar>!](./iousbhostcidevicespeedtostring%28_%29.md)
- [func IOUSBHostCIDeviceStateToString(IOUSBHostCIDeviceState) -> UnsafePointer<CChar>!](./iousbhostcidevicestatetostring%28_%29.md)
- [func IOUSBHostCIEndpointStateToString(IOUSBHostCIEndpointState) -> UnsafePointer<CChar>!](./iousbhostciendpointstatetostring%28_%29.md)
- [func IOUSBHostCIExceptionTypeToString(IOUSBHostCIExceptionType) -> UnsafePointer<CChar>!](./iousbhostciexceptiontypetostring%28_%29.md)
- [func IOUSBHostCILinkStateEnabled(IOUSBHostCILinkState) -> Bool](./iousbhostcilinkstateenabled%28_%29.md)
- [func IOUSBHostCILinkStateToString(IOUSBHostCILinkState) -> UnsafePointer<CChar>!](./iousbhostcilinkstatetostring%28_%29.md)
- [func IOUSBHostCIMessageStatusFromIOReturn(IOReturn) -> IOUSBHostCIMessageStatus](./iousbhostcimessagestatusfromioreturn%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcimessagestatustoioreturn(_:))*