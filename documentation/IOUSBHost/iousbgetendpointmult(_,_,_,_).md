# IOUSBGetEndpointMult(_:_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetEndpointMult(_ usbDeviceSpeed: UInt32, _ descriptor: UnsafePointer<IOUSBEndpointDescriptor>!, _ companionDescriptor: UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!, _ sspCompanionDescriptor: UnsafePointer<IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor>!) -> UInt8
```

## See Also

- [func IOUSBGetEndpointBurstSize(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!, UnsafePointer<IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor>!) -> UInt32](iousbgetendpointburstsize(_:_:_:_:).md)
- [func IOUSBGetEndpointSynchronizationType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointsynchronizationtype(_:).md)
- [func IOUSBGetEndpointUsageType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointusagetype(_:).md)
- [func IOUSBGetPlatformCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBPlatformCapabilityDescriptor>!](iousbgetplatformcapabilitydescriptor(_:).md)
- [func IOUSBGetPlatformCapabilityDescriptorWithUUID(UnsafePointer<IOUSBBOSDescriptor>!, UnsafeMutablePointer<UInt8>!) -> UnsafePointer<IOUSBPlatformCapabilityDescriptor>!](iousbgetplatformcapabilitydescriptorwithuuid(_:_:).md)
- [func IOUSBGetSuperSpeedPlusDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedPlusUSB>!](iousbgetsuperspeedplusdevicecapabilitydescriptor(_:).md)
- [func IOUSBHostCIControllerStateToString(IOUSBHostCIControllerState) -> UnsafePointer<CChar>!](iousbhostcicontrollerstatetostring(_:).md)
- [func IOUSBHostCIDeviceSpeedToString(IOUSBHostCIDeviceSpeed) -> UnsafePointer<CChar>!](iousbhostcidevicespeedtostring(_:).md)
- [func IOUSBHostCIDeviceStateToString(IOUSBHostCIDeviceState) -> UnsafePointer<CChar>!](iousbhostcidevicestatetostring(_:).md)
- [func IOUSBHostCIEndpointStateToString(IOUSBHostCIEndpointState) -> UnsafePointer<CChar>!](iousbhostciendpointstatetostring(_:).md)
- [func IOUSBHostCIExceptionTypeToString(IOUSBHostCIExceptionType) -> UnsafePointer<CChar>!](iousbhostciexceptiontypetostring(_:).md)
- [func IOUSBHostCILinkStateEnabled(IOUSBHostCILinkState) -> Bool](iousbhostcilinkstateenabled(_:).md)
- [func IOUSBHostCILinkStateToString(IOUSBHostCILinkState) -> UnsafePointer<CChar>!](iousbhostcilinkstatetostring(_:).md)
- [func IOUSBHostCIMessageStatusFromIOReturn(IOReturn) -> IOUSBHostCIMessageStatus](iousbhostcimessagestatusfromioreturn(_:).md)
- [func IOUSBHostCIMessageStatusToIOReturn(IOUSBHostCIMessageStatus) -> IOReturn](iousbhostcimessagestatustoioreturn(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetendpointmult(_:_:_:_:))*