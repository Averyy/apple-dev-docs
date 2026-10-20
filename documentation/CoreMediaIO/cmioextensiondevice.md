# CMIOExtensionDevice

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that represents a physical or virtual device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionDevice
```

```objc
@interface CMIOExtensionDevice : NSObject
```

## Mentions

- [Creating a camera extension with Core Media I/O](./creating-a-camera-extension-with-core-media-i-o.md)

#### Overview

A device provides one or more streams of media data to a [`CMIOExtensionProvider`](./cmioextensionprovider.md).

## Topics

### Creating a Device
- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](./cmioextensiondevice/init%28localizedname,deviceid,source%29.md)
  Creates an extension device.
- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](./cmioextensiondevice/init%28localizedname,deviceid,legacydeviceid,source%29.md)
  Creates an extension device with an optional legacy device identifier.
### Identifying a Device
- [var localizedName: String](./cmioextensiondevice/localizedname.md)
  A localized name for a device.
- [var deviceID: UUID](./cmioextensiondevice/deviceid.md)
  A universally unique device identifier value.
- [var legacyDeviceID: String](./cmioextensiondevice/legacydeviceid.md)
  A legacy device identifier.
### Managing Streams
- [var streams: [CMIOExtensionStream]](./cmioextensiondevice/streams.md)
  An array of media streams attached to this device.
- [func addStream(CMIOExtensionStream) throws](./cmioextensiondevice/addstream%28_%29.md)
  Adds a stream to a device.
- [func removeStream(CMIOExtensionStream) throws](./cmioextensiondevice/removestream%28_%29.md)
  Removes a stream from the device.
### Accessing the Device Source
- [var source: (any CMIOExtensionDeviceSource)?](./cmioextensiondevice/source.md)
  A source object for a device.
### Posting Property Changes
- [func notifyPropertiesChanged([CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./cmioextensiondevice/notifypropertieschanged%28_%29.md)
  Notifies clients of property changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [protocol CMIOExtensionDeviceSource](./cmioextensiondevicesource.md)
  A protocol for objects that act as device sources.
- [class CMIOExtensionDeviceProperties](./cmioextensiondeviceproperties.md)
  An object that defines the properties of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice)*