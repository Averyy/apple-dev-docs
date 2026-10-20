# HMAccessorySetupResult

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A result object describing information about a successful accessory setup request.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
class HMAccessorySetupResult
```

```objc
@interface HMAccessorySetupResult : NSObject
```

## Topics

### Getting results
- [var accessoryUniqueIdentifiers: [UUID]](./hmaccessorysetupresult/accessoryuniqueidentifiers.md)
  The values corresponding to accessories that are set up.
- [var homeUniqueIdentifier: UUID](./hmaccessorysetupresult/homeuniqueidentifier.md)
  The home that accessories were added to.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessories
- [class HMAccessorySetupManager](./hmaccessorysetupmanager.md)
  An object that setups up new accessories.
- [class HMAccessorySetupRequest](./hmaccessorysetuprequest.md)
  An object that describes how to add and setup up new accessories.
- [Interacting with a home automation network](./interacting-with-a-home-automation-network.md)
  Find all the automation accessories in the primary home and control their state.
- [class HMAccessory](./hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.
- [class HMService](./hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.
- [class HMCharacteristic](./hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- [class HMMediaSourceDisplayOrderProfile](./hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult)*