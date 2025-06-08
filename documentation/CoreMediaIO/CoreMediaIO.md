# Core Media I/O

**Framework**: Core Media I/O  
**Kind**: module

Securely support custom camera devices in macOS.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

#### Overview

Use the Core Media I/O framework to enable support for custom camera devices in macOS. Starting in macOS 12.3, the framework builds on [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) to enable you to support custom devices while maintaining system privacy and security protections. The system prevents apps from loading extension code into their process to ensure that they can’t bypass macOS privacy protections or mask their identity.

> ❗ **Important**: Apple recommends replacing legacy Device Abstraction Layer (DAL) plug-ins with Core Media I/O extensions.

## Topics

### Providers
- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)
  Build high-performance camera drivers that are secure and simple to deploy.
- [Overriding the default USB video class extension](overriding-the-default-usb-video-class-extension.md)
  Create a simple DriverKit extension to override the default driver-matching behavior for USB devices.
- [class CMIOExtensionProvider](cmioextensionprovider.md)
  An object that manages device connections for a provider.
- [protocol CMIOExtensionProviderSource](cmioextensionprovidersource.md)
  A protocol for objects that act as provider sources.
- [class CMIOExtensionProviderProperties](cmioextensionproviderproperties.md)
  An object that manages the properties of an extension provider.
### Devices
- [class CMIOExtensionDevice](cmioextensiondevice.md)
  An object that represents a physical or virtual device.
- [protocol CMIOExtensionDeviceSource](cmioextensiondevicesource.md)
  A protocol for objects that act as device sources.
- [class CMIOExtensionDeviceProperties](cmioextensiondeviceproperties.md)
  An object that defines the properties of a device.
### Streams
- [class CMIOExtensionStream](cmioextensionstream.md)
  An object that represents a stream of media data.
- [protocol CMIOExtensionStreamSource](cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionStreamProperties](cmioextensionstreamproperties.md)
  An object that describes the properties of an extension stream.
- [class CMIOExtensionClient](cmioextensionclient.md)
  An object that represents a client of the extension.
### Properties
- [struct CMIOExtensionProperty](cmioextensionproperty.md)
  A structure that defines the properties that providers, devices, and streams support.
- [class CMIOExtensionPropertyState](cmioextensionpropertystate.md)
  An object that describes the state of a property.
- [class CMIOExtensionPropertyAttributes](cmioextensionpropertyattributes.md)
  An object that describes the attributes of a property.
- [let CMIOExtensionInfoDictionaryKey: String](cmioextensioninfodictionarykey.md)
  A key that specifies the extension information dictionary.
- [let CMIOExtensionMachServiceNameKey: String](cmioextensionmachservicenamekey.md)
  A key that specifies the mach service name.
### DAL Plug-Ins
- [Device Abstraction Layer (DAL) Plug-Ins](device-abstraction-layer-dal-plug-ins.md)
  API reference for legacy DAL plug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreMediaIO)*