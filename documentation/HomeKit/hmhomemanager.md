# HMHomeManager

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMHomeManager : NSObject
```

## Mentions

- [Enabling HomeKit in your app](./enabling-homekit-in-your-app.md)

## Overview

HomeKit stores the user’s home automation information in a database that’s shared among Apple’s built-in iOS Home app, your HomeKit-enabled app, and apps from other developers. All these apps access the database as peers using the HomeKit framework.

![Diagram showing how different apps use HomeKit to access the shared HomeKit database.](https://developer.apple.com/tutorials/images/com.apple.homekit/media-3111423@2x.png)

Each app creates a single [`HMHomeManager`](./hmhomemanager.md) instance to coordinate its HomeKit-related activities. The manager’s [`homes`](./hmhomemanager/homes.md) array gives your app access to a collection of [`HMHome`](./hmhome.md) instances that represent the user’s homes. These in turn contain references to the home automation accessories that your app can inspect and control.

![Diagram showing a collection of homes within the home manager, each of which has a collection of accessories.](https://developer.apple.com/tutorials/images/com.apple.homekit/media-3111594@2x.png)

Adopt the [`HMHomeManagerDelegate`](./hmhomemanagerdelegate.md) protocol in your app to stay informed of any changes to the set of homes made outside your app.

## Topics

### Inspecting authorization status
- [var authorizationStatus: HMHomeManagerAuthorizationStatus](./hmhomemanager/authorizationstatus.md)
  The current state of the app’s access to home data.
- [struct HMHomeManagerAuthorizationStatus](./hmhomemanagerauthorizationstatus.md)
  The possible home-access states.
### Working with the home layout
- [var homes: [HMHome]](./hmhomemanager/homes.md)
  An array of all homes managed by this home manager.
- [class HMHome](./hmhome.md)
  The primary unit of living space, typically composed of rooms organized into zones.
### Keeping track of connected homes
- [var delegate: (any HMHomeManagerDelegate)?](./hmhomemanager/delegate.md)
  A delegate that receives updates on the collection of homes.
- [protocol HMHomeManagerDelegate](./hmhomemanagerdelegate.md)
  An interface the home manager uses to communicate changes to the state of the home network.
### Adding and removing homes
- [func addHome(withName: String, completionHandler: (HMHome?, (any Error)?) -> Void)](./hmhomemanager/addhome%28withname,completionhandler%29.md)
  Adds a new home to this home manager.
- [func removeHome(HMHome, completionHandler: ((any Error)?) -> Void)](./hmhomemanager/removehome%28_,completionhandler%29.md)
  Removes a home from this home manager.
### Providing installation services
- [func addProvisionalHome(named: String, configuration: HMHomeManager.ProvisionalConfiguration) async throws -> HMHome](./hmhomemanager/addprovisionalhome%28named,configuration%29.md)
  Adds a temporary provisional home while someone performs HomeKit installation services for a client.
- [HMHomeManager.ProvisionalConfiguration](./hmhomemanager/provisionalconfiguration.md)
  The configuration you use to create a temporary, provisional home for performing installation services.
- [HMHomeManager.PairingIdentity](./hmhomemanager/pairingidentity.md)
  Identity information that an installation service uses to set up a provisional home for a client.
### Finding vendor accessories
- [func findVendorAccessory(hapPublicKey: Data, completionHandler: (HMAccessory?, (any Error)?) -> Void)](./hmhomemanager/findvendoraccessory%28happublickey,completionhandler%29.md)
  Finds your vendor HAP accessory using its long-term public key.
### Deprecated
- [var primaryHome: HMHome?](./hmhomemanager/primaryhome.md)
  The primary home managed by this home manager.
- [func updatePrimaryHome(HMHome, completionHandler: ((any Error)?) -> Void)](./hmhomemanager/updateprimaryhome%28_,completionhandler%29.md)
  Updates the primary home of this home manager.
### Initializers
- [init()](./hmhomemanager/init%28%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Home Manager
- [Configuring a home automation device](./configuring-a-home-automation-device.md)
  Give users a familiar experience when they manage HomeKit accessories.
- [Testing your app with the HomeKit Accessory Simulator](./testing-your-app-with-the-homekit-accessory-simulator.md)
  Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager)*