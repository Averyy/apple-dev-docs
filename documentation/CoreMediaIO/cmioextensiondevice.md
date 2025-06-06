# CMIOExtensionDevice

**Framework**: Core Media I/O  
**Kind**: class

An object that represents a physical or virtual device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionDevice
```

## Mentions

- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)

#### Overview

A device provides one or more streams of media data to a [`CMIOExtensionProvider`](cmioextensionprovider.md).

## Topics

### Creating a Device
- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](cmioextensiondevice/init(localizedname:deviceid:source:).md)
  Creates an extension device.
- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](cmioextensiondevice/init(localizedname:deviceid:legacydeviceid:source:).md)
  Creates an extension device with an optional legacy device identifier.
### Identifying a Device
- [var localizedName: String](cmioextensiondevice/localizedname.md)
  A localized name for a device.
- [var deviceID: UUID](cmioextensiondevice/deviceid.md)
  A universally unique device identifier value.
- [var legacyDeviceID: String](cmioextensiondevice/legacydeviceid.md)
  A legacy device identifier.
### Managing Streams
- [var streams: [CMIOExtensionStream]](cmioextensiondevice/streams.md)
  An array of media streams attached to this device.
- [func addStream(CMIOExtensionStream) throws](cmioextensiondevice/addstream(_:).md)
  Adds a stream to a device.
- [func removeStream(CMIOExtensionStream) throws](cmioextensiondevice/removestream(_:).md)
  Removes a stream from the device.
### Accessing the Device Source
- [var source: (any CMIOExtensionDeviceSource)?](cmioextensiondevice/source.md)
  A source object for a device.
### Posting Property Changes
- [func notifyPropertiesChanged([CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensiondevice/notifypropertieschanged(_:).md)
  Notifies clients of property changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol CMIOExtensionDeviceSource](cmioextensiondevicesource.md)
  A protocol for objects that act as device sources.
- [class CMIOExtensionDeviceProperties](cmioextensiondeviceproperties.md)
  An object that defines the properties of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice)*