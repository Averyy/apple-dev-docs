# HMAccessorySetupRequest

**Framework**: HomeKit  
**Kind**: class

An object that describes how to add and setup up new accessories.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Declaration

```swift
class HMAccessorySetupRequest
```

#### Overview

Use this class to provide steps for the user to add one or more accessories to a particular home, and follow up with additional setup.

## Topics

### Setting up accessorices
- [var homeUniqueIdentifier: UUID?](hmaccessorysetuprequest/homeuniqueidentifier.md)
  The identifier corresponding to the home that the accessory should be added to when being set up.
- [var payload: HMAccessorySetupPayload?](hmaccessorysetuprequest/payload.md)
  The payload to use for accessory setup.
- [var suggestedAccessoryName: String?](hmaccessorysetuprequest/suggestedaccessoryname.md)
  The name that the framework suggests when the user names the accessory being set up.
- [var suggestedRoomUniqueIdentifier: UUID?](hmaccessorysetuprequest/suggestedroomuniqueidentifier.md)
  The identifier corresponding to the room that the framework suggests.
### Instance Properties
- [var matterPayload: MTRSetupPayload?](hmaccessorysetuprequest/matterpayload.md)
### Initializers
- [init()](hmaccessorysetuprequest/init.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMAccessorySetupManager](hmaccessorysetupmanager.md)
  An object that setups up new accessories.
- [class HMAccessorySetupResult](hmaccessorysetupresult.md)
  A result object describing information about a successful accessory setup request.
- [Interacting with a home automation network](interacting-with-a-home-automation-network.md)
  Find all the automation accessories in the primary home and control their state.
- [class HMAccessory](hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.
- [class HMService](hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest)*