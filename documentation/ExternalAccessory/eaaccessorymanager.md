# EAAccessoryManager

**Framework**: External Accessory  
**Kind**: class  
**Role**: Class

The object you use to identify connected accessories, and begin delivery of connection and disconnection notifications.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class EAAccessoryManager
```

```objc
@interface EAAccessoryManager : NSObject
```

## Overview

An [`EAAccessoryManager`](./eaaccessorymanager.md) object coordinates the attached accessories for an iOS-based device. Use the shared accessory manager to retrieve a list of connected accessories, and start and stop the delivery of connection and disconnection notifications.

> ❗ **Important**:  iPhone and iPad apps running on Macs with Apple silicon never receive connection notifications.

## Topics

### Getting the Shared Accessory Manager
- [class func shared() -> EAAccessoryManager](./eaaccessorymanager/shared%28%29.md)
  Returns the shared accessory manager object for the iOS-based device.
### Managing Connection Status Changes
- [func registerForLocalNotifications()](./eaaccessorymanager/registerforlocalnotifications%28%29.md)
  Begins the delivery of accessory-related notifications to the current application.
- [func unregisterForLocalNotifications()](./eaaccessorymanager/unregisterforlocalnotifications%28%29.md)
  Stops the delivery of accessory-related notifications to the current application.
- [static let EAAccessoryDidConnect: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
- [let EAAccessoryKey: String](./eaaccessorykey.md)
  A key that indicates the accessory object whose status changed.
- [let EAAccessorySelectedKey: String](./eaaccessoryselectedkey.md)
  A key that indicates the accessory object that the user selected.
- [EAAccessoryDidConnectNotification](./eaaccessorydidconnectnotification.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [EAAccessoryDidDisconnectNotification](./eaaccessorydiddisconnectnotification.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
### Presenting the Bluetooth Picker
- [func showBluetoothAccessoryPicker(withNameFilter: NSPredicate?, completion: (((any Error)?) -> Void)?)](./eaaccessorymanager/showbluetoothaccessorypicker%28withnamefilter,completion%29.md)
  Displays an alert that allows the user to pair the device with a Bluetooth accessory.
- [typealias EABluetoothAccessoryPickerCompletion](./eabluetoothaccessorypickercompletion.md)
  The completion block for the Bluetooth picker.
- [struct EABluetoothAccessoryPickerError](./eabluetoothaccessorypickererror.md)
  Error codes returned by the Bluetooth accessory picker.
- [EABluetoothAccessoryPickerError.Code](./eabluetoothaccessorypickererror/code.md)
  The error codes that may be passed in an error object for the Bluetooth picker completion block.
- [let EABluetoothAccessoryPickerErrorDomain: String](./eabluetoothaccessorypickererrordomain.md)
  The domain for errors passed to a Bluetooth picker completion block.
### Getting the Available Accessories
- [var connectedAccessories: [EAAccessory]](./eaaccessorymanager/connectedaccessories.md)
  The accessory objects corresponding to the list of currently connected accessories.
### Structures
- [EAAccessoryManager.AccessoryDidConnectMessage](./eaaccessorymanager/accessorydidconnectmessage.md)
- [EAAccessoryManager.AccessoryDidDisconnectMessage](./eaaccessorymanager/accessorydiddisconnectmessage.md)

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

### Essentials
- [UISupportedExternalAccessoryProtocols](../BundleResources/information-property-list/uisupportedexternalaccessoryprotocols.md)
  The protocols that the app uses to communicate with external accessory hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager)*