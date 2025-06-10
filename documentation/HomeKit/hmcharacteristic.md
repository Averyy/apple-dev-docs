# HMCharacteristic

**Framework**: HomeKit  
**Kind**: class

A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMCharacteristic
```

#### Overview

An [`HMCharacteristic`](hmcharacteristic.md) instance represents an aspect of a service that provides data, or that your app can control.

You don’t create characteristic instances. Instead, an accessory manufacturer incorporates them into a device, which publishes them to you through the [`characteristics`](hmservice/characteristics.md) array of an [`HMService`](hmservice.md) instance.

Characteristics have a [`properties`](hmcharacteristic/properties.md) array that indicates attributes like readability, writability, and user-visibility. They also have a [`characteristicType`](hmcharacteristic/characteristictype.md) property that tells your app what the characteristic controls or describes. Device manufacturers can use one of the standard types, given in [`Characteristic types`](characteristic-types.md), or they can create custom types.

Each characteristic has a [`value`](hmcharacteristic/value.md) that you can read or write. Some characteristics use plain numbers, Booleans, or strings. Others have application specific meanings declared in enumerations associated with the given characteristic type. The characteristic’s [`metadata`](hmcharacteristic/metadata.md) can help your app interpret the value.

## Topics

### Identifying a characteristic
- [var uniqueIdentifier: UUID](hmcharacteristic/uniqueidentifier.md)
  A unique identifier for the characteristic.
- [var localizedDescription: String](hmcharacteristic/localizeddescription.md)
  The localized description of the characteristic.
### Reading characteristic properties
- [var properties: [String]](hmcharacteristic/properties.md)
  An array of properties that describe the characteristic.
- [Characteristic Properties](characteristic-properties.md)
  The properties that characteristics can have.
### Determining what a characteristic controls
- [var characteristicType: String](hmcharacteristic/characteristictype.md)
  The type of the characteristic.
- [Characteristic types](characteristic-types.md)
  The characteristic types supported by HomeKit-based accessories.
### Controlling a characteristic
- [var value: Any?](hmcharacteristic/value.md)
  The current value of the characteristic.
- [func readValue(completionHandler: ((any Error)?) -> Void)](hmcharacteristic/readvalue(completionhandler:).md)
  Reads the value for the characteristic.
- [func writeValue(Any?, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/writevalue(_:completionhandler:).md)
  Modifies the value of the characteristic.
- [func updateAuthorizationData(Data?, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/updateauthorizationdata(_:completionhandler:).md)
  Sets or clears authorization data used when writing to the characteristic.
### Managing characteristic presentation
- [var metadata: HMCharacteristicMetadata?](hmcharacteristic/metadata.md)
  Metadata about the units and other properties of the characteristic.
- [class HMCharacteristicMetadata](hmcharacteristicmetadata.md)
  Metadata that describes a characteristic’s value and that may be useful for presentation purposes.
### Receiving change notifications
- [func enableNotification(Bool, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/enablenotification(_:completionhandler:).md)
  Enables or disables notifications for changes in the value of the characteristic.
- [var isNotificationEnabled: Bool](hmcharacteristic/isnotificationenabled.md)
  A Boolean indicating whether the characteristic has been set to send notifications.
### Getting the characterized service
- [var service: HMService?](hmcharacteristic/service.md)
  The service that contains this characteristic.
### Initializers
- [init()](hmcharacteristic/init.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMAccessorySetupManager](hmaccessorysetupmanager.md)
  An object that setups up new accessories.
- [class HMAccessorySetupResult](hmaccessorysetupresult.md)
  A result object describing information about a successful accessory setup request.
- [class HMAccessorySetupRequest](hmaccessorysetuprequest.md)
  An object that describes how to add and setup up new accessories.
- [Interacting with a home automation network](interacting-with-a-home-automation-network.md)
  Find all the automation accessories in the primary home and control their state.
- [class HMAccessory](hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.
- [class HMService](hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic)*