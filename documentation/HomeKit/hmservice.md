# HMService

**Framework**: HomeKit  
**Kind**: class

A controllable feature of an accessory, like a light attached to a garage door opener.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMService
```

#### Overview

An [`HMService`](hmservice.md) instance represents a service provided by an accessory. Accessories have both user-controllable services, like a light, and services that are for the use of the accessory itself, like a firmware update service.

You don’t create services directly. Instead you find them in the [`services`](hmaccessory/services.md) array of an [`HMAccessory`](hmaccessory.md) instance.

A single accessory may have more than one user-controllable service. For example, most garage door openers have a service for opening and closing the door, and another service for the light on the garage door opener. These services are what Apple’s Home app labels as “accessories”.

You inspect or change a service’s [`HMCharacteristic`](hmcharacteristic.md) instances to discover state, or modify behavior.

## Topics

### Getting service characteristics
- [var characteristics: [HMCharacteristic]](hmservice/characteristics.md)
  An array of characteristics for the service.
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
### Identifying the service
- [var name: String](hmservice/name.md)
  The user specified name of the service.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmservice/updatename(_:completionhandler:).md)
  Updates the name of the service to the specified string.
- [var uniqueIdentifier: UUID](hmservice/uniqueidentifier.md)
  A unique identifier for the service.
### Getting the service type
- [var serviceType: String](hmservice/servicetype.md)
  The type of the service.
- [Accessory Service Types](accessory-service-types.md)
  The service types supported by HomeKit.
- [var localizedDescription: String](hmservice/localizeddescription.md)
  The localized description of the service.
### Reading service properties
- [var isPrimaryService: Bool](hmservice/isprimaryservice.md)
  A Boolean value that indicates whether this service is the primary service on the accessory.
- [var isUserInteractive: Bool](hmservice/isuserinteractive.md)
  A Boolean value that indicates whether this service supports user interaction.
### Associating a secondary service
- [var associatedServiceType: String?](hmservice/associatedservicetype.md)
  The type of the service associated with an outlet or a switch.
- [func updateAssociatedServiceType(String?, completionHandler: ((any Error)?) -> Void)](hmservice/updateassociatedservicetype(_:completionhandler:).md)
  Associates the service type of the plugged-in device with a switch or an outlet service.
### Finding the linked services
- [var linkedServices: [HMService]?](hmservice/linkedservices.md)
  An array of service objects that represents all the services to which the service links.
### Getting the service’s provider
- [var accessory: HMAccessory?](hmservice/accessory.md)
  The accessory that provides this service.
### Initializers
- [init()](hmservice/init.md)
### Instance Properties
- [var matterEndpointID: UInt16?](hmservice/matterendpointid-62vu6.md)

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
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice)*