# Parsing USB Descriptors

**Framework**: IOUSBHost

Extract information from various USB descriptors using helper methods.

## Topics

### Configuration Descriptor Parsing
- [func IOUSBGetNextDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextdescriptor(_:_:).md)
  Obtains the next descriptor in a configuration descriptor.
- [func IOUSBGetNextDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextdescriptorwithtype(_:_:_:).md)
  Obtains the next descriptor in a configuration descriptor that matches the type.
- [func IOUSBGetNextAssociatedDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextassociateddescriptor(_:_:_:).md)
  Obtains the next associated descriptor in a configuration descriptor.
- [func IOUSBGetNextAssociatedDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextassociateddescriptorwithtype(_:_:_:_:).md)
  Obtains the next associated descriptor in a configuration descriptor and matches the type.
- [func IOUSBGetNextInterfaceAssociationDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceAssociationDescriptor>!](iousbgetnextinterfaceassociationdescriptor(_:_:).md)
  Obtains the next interface association descriptor in a configuration descriptor.
- [func IOUSBGetNextInterfaceDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceDescriptor>!](iousbgetnextinterfacedescriptor(_:_:).md)
  Obtains the next interface descriptor in a configuration descriptor.
- [func IOUSBGetConfigurationMaxPowerMilliAmps(UInt32, UnsafePointer<IOUSBConfigurationDescriptor>!) -> UInt32](iousbgetconfigurationmaxpowermilliamps(_:_:).md)
  Obtains the maximum bus current that a configuration descriptor requires.
### BOS Descriptor Parsing
- [func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!](iousbgetusb20extensiondevicecapabilitydescriptor(_:).md)
  Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptorWithType(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptorwithtype(_:_:_:).md)
  Obtains the next descriptor matching a specific type within a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptor(_:_:).md)
  Obtains the next device capability descriptor in a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](iousbgetsuperspeeddevicecapabilitydescriptor(_:).md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](iousbgetcontaineriddescriptor(_:).md)
  Obtains the first container ID capability descriptor in a BOS descriptor.
- [func IOUSBGetBillboardDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!](iousbgetbillboarddescriptor(_:).md)
  Obtains the first billboard capability descriptor in a BOS descriptor.
### Endpoint Descriptor Parsing
- [func IOUSBGetNextEndpointDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBInterfaceDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBEndpointDescriptor>!](iousbgetnextendpointdescriptor(_:_:_:).md)
  Obtains the next endpoint descriptor for an interface descriptor.
- [func IOUSBGetEndpointDirection(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointdirection(_:).md)
  Obtains the direction of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointAddress(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointaddress(_:).md)
  Obtains the direction and number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointNumber(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointnumber(_:).md)
  Obtains the number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointtype(_:).md)
  Obtains the type of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointMaxPacketSize(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt16](iousbgetendpointmaxpacketsize(_:_:).md)
  Obtains the maximum packet size from an endpoint descriptor.
- [func IOUSBGetEndpointIntervalEncodedMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalencodedmicroframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalmicroframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalFrames(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointMaxStreamsEncoded(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](iousbgetendpointmaxstreamsencoded(_:_:_:).md)
  Obtains the number of streams that an endpoint supports.
- [func IOUSBGetEndpointMaxStreams(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](iousbgetendpointmaxstreams(_:_:_:).md)
  Obtains the number of supported streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/parsing-usb-descriptors)*