# HKDevice

**Framework**: HealthKit  
**Kind**: class

A device that generates data for HealthKit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKDevice
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

Devices include Apple Watch, iPhone, and any other health or fitness peripherals that produce the sample data stored in HealthKit. Device objects are immutable: You set the device’s properties when you create the [`HKDevice`](hkdevice.md) object, and they cannot change.

## Topics

### Creating Device Objects
- [init(name: String?, manufacturer: String?, model: String?, hardwareVersion: String?, firmwareVersion: String?, softwareVersion: String?, localIdentifier: String?, udiDeviceIdentifier: String?)](hkdevice/init(name:manufacturer:model:hardwareversion:firmwareversion:softwareversion:localidentifier:udideviceidentifier:).md)
  Initializes a new device object.
- [class func local() -> HKDevice](hkdevice/local.md)
  returns a device object that represents the current device.
### Accessing Data About a Device
- [var udiDeviceIdentifier: String?](hkdevice/udideviceidentifier.md)
  The device identifier portion of the US Food and Drug Administration’s Unique Device Identifier (UDI).
- [var firmwareVersion: String?](hkdevice/firmwareversion.md)
  An arbitrary string representing the current version of the firmware running on the device.
- [var hardwareVersion: String?](hkdevice/hardwareversion.md)
  An arbitrary string representing the hardware version of the device.
- [var localIdentifier: String?](hkdevice/localidentifier.md)
  An identifier that uniquely identifies the device object on the hardware running this code.
- [var manufacturer: String?](hkdevice/manufacturer.md)
  A string representing the device’s manufacturer.
- [var model: String?](hkdevice/model.md)
  A string representing the device’s model.
- [var name: String?](hkdevice/name.md)
  The user-facing name for the device.
- [var softwareVersion: String?](hkdevice/softwareversion.md)
  An arbitrary string representing the version of the software running on the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HKSourceQueryDescriptor](hksourcequerydescriptor.md)
  A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.
- [class HKSourceRevision](hksourcerevision.md)
  An object indicating the source of a HealthKit sample.
- [class HKSource](hksource.md)
  An object indicating the app or device that created a HealthKit sample
- [class HKSourceQuery](hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdevice)*