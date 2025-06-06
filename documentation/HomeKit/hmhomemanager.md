# HMHomeManager

**Framework**: HomeKit  
**Kind**: class

The manager for a collection of one or more of a user’s homes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMHomeManager
```

## Mentions

- [Enabling HomeKit in your app](enabling-homekit-in-your-app.md)

#### Overview

HomeKit stores the user’s home automation information in a database that’s shared among Apple’s built-in iOS Home app, your HomeKit-enabled app, and apps from other developers. All these apps access the database as peers using the HomeKit framework.

![Diagram showing how different apps use HomeKit to access the shared HomeKit database.](https://docs-assets.developer.apple.com/published/1d1af3529d72cebfde9b21706f91cb43/media-3111423%402x.png)

Each app creates a single [`HMHomeManager`](hmhomemanager.md) instance to coordinate its HomeKit-related activities. The manager’s [`homes`](hmhomemanager/homes.md) array gives your app access to a collection of [`HMHome`](hmhome.md) instances that represent the user’s homes. These in turn contain references to the home automation accessories that your app can inspect and control.

![Diagram showing a collection of homes within the home manager, each of which has a collection of accessories.](https://docs-assets.developer.apple.com/published/0a853498ff99cc139c55fe113f1169a1/media-3111594%402x.png)

Adopt the [`HMHomeManagerDelegate`](hmhomemanagerdelegate.md) protocol in your app to stay informed of any changes to the set of homes made outside your app.

## Topics

### Inspecting authorization status
- [var authorizationStatus: HMHomeManagerAuthorizationStatus](hmhomemanager/authorizationstatus.md)
  The current state of the app’s access to home data.
- [struct HMHomeManagerAuthorizationStatus](hmhomemanagerauthorizationstatus.md)
  The possible home-access states.
### Working with the home layout
- [var homes: [HMHome]](hmhomemanager/homes.md)
  An array of all homes managed by this home manager.
- [class HMHome](hmhome.md)
  The primary unit of living space, typically composed of rooms organized into zones.
### Keeping track of connected homes
- [var delegate: (any HMHomeManagerDelegate)?](hmhomemanager/delegate.md)
  A delegate that receives updates on the collection of homes.
- [protocol HMHomeManagerDelegate](hmhomemanagerdelegate.md)
  An interface the home manager uses to communicate changes to the state of the home network.
### Adding and removing homes
- [func addHome(withName: String, completionHandler: (HMHome?, (any Error)?) -> Void)](hmhomemanager/addhome(withname:completionhandler:).md)
  Adds a new home to this home manager.
- [func removeHome(HMHome, completionHandler: ((any Error)?) -> Void)](hmhomemanager/removehome(_:completionhandler:).md)
  Removes a home from this home manager.
### Managing the primary home
- [var primaryHome: HMHome?](hmhomemanager/primaryhome.md)
  The primary home managed by this home manager.
- [func updatePrimaryHome(HMHome, completionHandler: ((any Error)?) -> Void)](hmhomemanager/updateprimaryhome(_:completionhandler:).md)
  Updates the primary home of this home manager.
### Initializers
- [init()](hmhomemanager/init.md)

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

- [Configuring a home automation device](configuring-a-home-automation-device.md)
  Give users a familiar experience when they manage HomeKit accessories.
- [Testing your app with the HomeKit Accessory Simulator](testing-your-app-with-the-homekit-accessory-simulator.md)
  Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager)*