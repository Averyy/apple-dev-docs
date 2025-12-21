# HMAccessory

**Framework**: HomeKit  
**Kind**: class

A home automation accessory, like a garage door opener or a thermostat.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMAccessory
```

#### Overview

An [`HMAccessory`](hmaccessory.md) instance represents a physical device, like a garage door opener, installed in a home and assigned to a room.

You don’t create accessories directly. Instead you get them from the [`accessories`](hmhome/accessories.md) array of an [`HMHome`](hmhome.md) instance when you want all the accessories in a home, or the [`accessories`](hmroom/accessories.md) array of an [`HMRoom`](hmroom.md) instance when you want all the accessories in a particular room. Each physical accessory in the home is represented by exactly one accessory instance, so that one instance appears in both a home and a room collection. This is because it’s simultaneously part of the home and in one of the home’s rooms.

When you want to add new accessories, you call the home’s [`addAndSetupAccessories(completionHandler:)`](hmhome/addandsetupaccessories(completionhandler:).md) method. In response, HomeKit presents the user with an interface that steps through the process of searching for new accessories in the physical environment, naming them, and assigning them to a room.

Accessories provide one or more services, represented by instances of [`HMService`](hmservice.md), that are the features that the user can control, like the light attached to a garage door opener, or the door opener mechanism itself.

## Topics

### Tracking changes to an accessory
- [var delegate: (any HMAccessoryDelegate)?](hmaccessory/delegate.md)
  A delegate that receives updates on the state of the accessory.
- [protocol HMAccessoryDelegate](hmaccessorydelegate.md)
  A set of methods that defines the communication method for state updates from accessories to their delegates.
### Identifying an Accessory
- [var name: String](hmaccessory/name.md)
  The name of the accessory.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmaccessory/updatename(_:completionhandler:).md)
  Changes the name of the accessory.
- [var uniqueIdentifier: UUID](hmaccessory/uniqueidentifier.md)
  A unique identifier for the accessory.
- [var identifier: UUID](hmaccessory/identifier.md)
  A unique identifier for the accessory.
### Categorizing an accessory
- [var category: HMAccessoryCategory](hmaccessory/category.md)
  The category to which the accessory belongs.
- [class HMAccessoryCategory](hmaccessorycategory.md)
  A category for a HomeKit accessory.
### Locating an accessory
- [var room: HMRoom?](hmaccessory/room.md)
  The room containing the accessory.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.
### Managing accessory profiles
- [var profiles: [HMAccessoryProfile]](hmaccessory/profiles.md)
  An array of profiles implemented by the accessory.
- [class HMAccessoryProfile](hmaccessoryprofile.md)
  A profile that certain accessories implement.
- [class HMNetworkConfigurationProfile](hmnetworkconfigurationprofile.md)
  A profile that provides information about network protection for an accessory.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.
### Managing camera profiles
- [struct CameraView](cameraview.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [var cameraProfiles: [HMCameraProfile]?](hmaccessory/cameraprofiles.md)
  An array of camera profiles implemented by the accessory.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.
- [class HMCameraView](hmcameraview.md)
  The view into which a video stream or an image snapshot is rendered.
### Getting accessory state
- [var isReachable: Bool](hmaccessory/isreachable.md)
  A Boolean value indicating whether the accessory can be communicated with in the current network environment.
- [var isBlocked: Bool](hmaccessory/isblocked.md)
  A Boolean value indicating whether the accessory is blocked.
### Asking an accessory to identify itself
- [var supportsIdentify: Bool](hmaccessory/supportsidentify.md)
  A Boolean value that indicates whether the accessory supports the identify action.
- [func identify(completionHandler: ((any Error)?) -> Void)](hmaccessory/identify(completionhandler:).md)
  Asks an accessory to identify itself.
### Controlling accessory features
- [var services: [HMService]](hmaccessory/services.md)
  An array of services provided by the accessory.
- [class HMService](hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.
### Managing bridged accessories
- [var isBridged: Bool](hmaccessory/isbridged.md)
  A Boolean that indicates whether the accessory is accessed through a bridge.
- [var uniqueIdentifiersForBridgedAccessories: [UUID]?](hmaccessory/uniqueidentifiersforbridgedaccessories.md)
  An array of unique identifiers, each of which represents an accessory vended by the bridge.
- [var identifiersForBridgedAccessories: [UUID]?](hmaccessory/identifiersforbridgedaccessories.md)
  An array of identifiers for accessories available through a bridge.
### Getting manufacturer information
- [var firmwareVersion: String?](hmaccessory/firmwareversion.md)
  The firmware version of the accessory.
- [var manufacturer: String?](hmaccessory/manufacturer.md)
  The manufacturer of the accessory.
- [var model: String?](hmaccessory/model.md)
  The model name of the accessory.
### Browsing for accessories
- [class HMAccessoryBrowser](hmaccessorybrowser.md)
  A network browser you can use to discover new accessories in a home.
### Instance Properties
- [var matterNodeID: UInt64?](hmaccessory/matternodeid-67v1j.md)
- [var bridgedAccessories: [HMAccessory]](hmaccessory/bridgedaccessories.md)
- [var hapInstanceID: UInt64?](hmaccessory/hapinstanceid-3cusx.md)
- [var home: HMHome?](hmaccessory/home.md)
- [var isVendorAccessory: Bool](hmaccessory/isvendoraccessory.md)
### Initializers
- [init()](hmaccessory/init.md)

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
- [class HMService](hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.
- [class HMCharacteristic](hmcharacteristic.md)
  A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory)*