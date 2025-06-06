# HMAccessorySetupManager

**Framework**: HomeKit  
**Kind**: class

An object that setups up new accessories.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
class HMAccessorySetupManager
```

#### Overview

Use this class to provides steps for the user to add one or more accessories to a particular home, and follow up with additional setup. These APIs don’t require that the current app has home data authorization.

## Topics

### Adding accessories
- [func performAccessorySetup(using: HMAccessorySetupRequest, completionHandler: (HMAccessorySetupResult?, (any Error)?) -> Void)](hmaccessorysetupmanager/performaccessorysetup(using:completionhandler:).md)
  Performs the process of setting up accessories with Apple Home.
### Initializers
- [init()](hmaccessorysetupmanager/init.md)

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
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager)*