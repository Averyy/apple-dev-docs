# HMMediaSourceDisplayOrderProfile

**Framework**: HomeKit  
**Kind**: class

An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@objc
class HMMediaSourceDisplayOrderProfile
```

#### Overview

This class represents a media source display that orders functionality for the [`HMServiceTypeTelevision`](hmservicetypetelevision.md) service contained in the services array of the profile.

## Topics

### Managing input source order
- [func writeOrder([Int]) async throws](hmmediasourcedisplayorderprofile/writeorder(_:).md)
  Writes the display order of the media sources to the accessory.
- [var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?](hmmediasourcedisplayorderprofile/delegate-swift.property.md)
  The property that handles updates to the display order.
- [var order: [Int]](hmmediasourcedisplayorderprofile/order.md)
  The display order of input media sources.
- [let canModifyOrder: Bool](hmmediasourcedisplayorderprofile/canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.
- [HMMediaSourceDisplayOrderProfile.Delegate](hmmediasourcedisplayorderprofile/delegate-swift.protocol.md)
  The protocol through which a delegate receives updates on the order of input media sources.

## Relationships

### Inherits From
- [HMAccessoryProfile](hmaccessoryprofile.md)
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
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile)*