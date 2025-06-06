# UIDevice

**Framework**: UIKit  
**Kind**: class

A representation of the current device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDevice
```

#### Overview

Use a [`UIDevice`](uidevice.md) object to get information about the device such as assigned name, device model, and operating-system name and version. You also use the `UIDevice` instance to detect changes in the device’s characteristics, such as physical orientation. You get the current orientation using the [`orientation`](uidevice/orientation.md) property or receive change notifications by registering for the [`orientationDidChangeNotification`](uidevice/orientationdidchangenotification.md) notification. Before using either of these techniques to get orientation data, you must enable data delivery using the [`beginGeneratingDeviceOrientationNotifications()`](uidevice/begingeneratingdeviceorientationnotifications().md) method. When you no longer need to track the device orientation, call the [`endGeneratingDeviceOrientationNotifications()`](uidevice/endgeneratingdeviceorientationnotifications().md) method to disable the delivery of notifications.

Similarly, you can use the `UIDevice` instance to obtain information and notifications about changes to the battery’s charge state (described by the [`batteryState`](uidevice/batterystate-swift.property.md) property) and charge level (described by the [`batteryLevel`](uidevice/batterylevel.md) property). The `UIDevice` instance also provides access to the proximity sensor state (described by the [`proximityState`](uidevice/proximitystate.md) property). The proximity sensor detects whether the user is holding the device close to their face. Enable battery monitoring or proximity sensing only when you need it.

You can also use the [`playInputClick()`](uidevice/playinputclick().md) instance method to play keyboard input clicks in custom input and keyboard accessory views.

## Topics

### Getting the shared device instance
- [class var current: UIDevice](uidevice/current.md)
  An object that represents the current device.
### Identifying the device and operating system
- [var name: String](uidevice/name.md)
  The name of the device.
- [var systemName: String](uidevice/systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](uidevice/systemversion.md)
  The current version of the operating system.
- [var model: String](uidevice/model.md)
  The model of the device.
- [var localizedModel: String](uidevice/localizedmodel.md)
  The model of the device as a localized string.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uidevice/userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](uidevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.
### Determining the available features
- [var isMultitaskingSupported: Bool](uidevice/ismultitaskingsupported.md)
  A Boolean value that indicates whether the current device supports multitasking.
### Tracking the device orientation
- [var orientation: UIDeviceOrientation](uidevice/orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](uidevice/isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](uidevice/begingeneratingdeviceorientationnotifications.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](uidevice/endgeneratingdeviceorientationnotifications.md)
  Ends the generation of notifications of device orientation changes.
### Determining the current orientation
- [var isPortrait: Bool](uideviceorientation/isportrait.md)
  A Boolean value that indicates whether the device is in a portrait orientation.
- [var isLandscape: Bool](uideviceorientation/islandscape.md)
  A Boolean value that indicates whether the device is in a landscape orientation.
- [var isFlat: Bool](uideviceorientation/isflat.md)
  A Boolean value that indicates whether the specified orientation is face up or face down.
- [var isValidInterfaceOrientation: Bool](uideviceorientation/isvalidinterfaceorientation.md)
  A Boolean value that indicates whether the specified orientation is one of the portrait or landscape orientations.
### Getting the device battery state
- [var batteryLevel: Float](uidevice/batterylevel.md)
  The battery charge level for the device.
- [var isBatteryMonitoringEnabled: Bool](uidevice/isbatterymonitoringenabled.md)
  A Boolean value that indicates whether battery monitoring is enabled.
- [var batteryState: UIDevice.BatteryState](uidevice/batterystate-swift.property.md)
  The battery state for the device.
- [UIDevice.BatteryState](uidevice/batterystate-swift.enum.md)
  Constants that describe the battery power state of the device.
### Using the proximity sensor
- [var isProximityMonitoringEnabled: Bool](uidevice/isproximitymonitoringenabled.md)
  A Boolean value that indicates whether proximity monitoring is enabled.
- [var proximityState: Bool](uidevice/proximitystate.md)
  A Boolean value that indicates whether the proximity sensor is close to the user.
### Playing input clicks
- [func playInputClick()](uidevice/playinputclick.md)
  Plays an input click in an enabled input view.
### Getting the current idiom
- [enum UIUserInterfaceIdiom](uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom](ui_user_interface_idiom().md)
  Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).
### Managing notifications
- [class let batteryLevelDidChangeNotification: NSNotification.Name](uidevice/batteryleveldidchangenotification.md)
  A notification that posts when the battery level changes.
- [class let batteryStateDidChangeNotification: NSNotification.Name](uidevice/batterystatedidchangenotification.md)
  A notification that posts when battery state changes.
- [class let orientationDidChangeNotification: NSNotification.Name](uidevice/orientationdidchangenotification.md)
  A notification that posts when the orientation of the device changes.
- [class let proximityStateDidChangeNotification: NSNotification.Name](uidevice/proximitystatedidchangenotification.md)
  A notification that posts when the state of the proximity sensor changes.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIStatusBarManager](uistatusbarmanager.md)
  An object that describes the configuration of the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice)*