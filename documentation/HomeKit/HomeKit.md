# HomeKit

**Framework**: HomeKit  
**Kind**: module

Configure, control, and communicate with home automation accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

![The diagram depicts a stylized phone emitting waves to indicate communication with a house pictured as a central icon. Four icons are arranged in a semi-circle to the right of the house icon, depicting connected accessories including a garage door, a thermometer, a sliding light switch, and a lamp.](https://docs-assets.developer.apple.com/published/d33b070d6684f4f8ae1ed27b980f946b/media-3111422%402x.png)

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database.
- Display, edit, and act upon the data in the home configuration database.
- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room.

## Topics

### Essentials
- [Enabling HomeKit in your app](enabling-homekit-in-your-app.md)
  Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.
- [HomeKit Entitlement](../BundleResources/Entitlements/com.apple.developer.homekit.md)
  A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- [NSHomeKitUsageDescription](../BundleResources/Information-Property-List/NSHomeKitUsageDescription.md)
  A message that tells people why the app is requesting access to their HomeKit configuration data.
### Home Manager
- [Configuring a home automation device](configuring-a-home-automation-device.md)
  Give users a familiar experience when they manage HomeKit accessories.
- [Testing your app with the HomeKit Accessory Simulator](testing-your-app-with-the-homekit-accessory-simulator.md)
  Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.
- [class HMHomeManager](hmhomemanager.md)
  The manager for a collection of one or more of a user’s homes.
### Accessories
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
- [class HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
  An interface from which to read and, if allowed by the accessory, update the ordering of input sources.
### Action Sets
- [class HMActionSet](hmactionset.md)
  A collection of actions that you trigger as a group.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
### Errors
- [struct HMError](hmerror.md)
  An error HomeKit returns.
- [let HMErrorDomain: String](hmerrordomain.md)
  A string that identifies the HomeKit error domain.
- [HMError.Code](hmerror/code.md)
  Possible error values that can be returned from HomeKit APIs.
- [typealias HMErrorBlock](hmerrorblock.md)
  A completion block that provides an error.
### Classes
- [class HMAccessorySetupPayload](hmaccessorysetuppayload.md)
  A payload for authenticating a HomeKit accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HomeKit)*