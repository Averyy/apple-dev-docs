# Accessory Live Activities

**Framework**: Accessory Live Activities  
**Kind**: module

Forward Live Activity alerts from iPhone to an accessory you develop.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

#### Overview

With the Accessory Live Activities framework, your accessory companion app can request Live Activity forwarding from people and receive Live Activity status updates and alerts from the system through an extension model. Your accessory can then display Live Activity status information and an alert that provides people with information about the updated Live Activity.

People can choose to forward Live Activities from all apps, no apps, or a subset of apps on their iPhone. When people set up your accessory, the system presents a prompt to configure these preferences for both Live Activity and iOS system notification forwarding. To add support for Live Activity forwarding, you also implement iOS system notification forwarding with the [`Accessory Notifications`](https://developer.apple.com/documentation/AccessoryNotifications) framework. Start by adding support for notification forwarding, then add support for Live Activity forwarding.

> ❗ **Important**: This framework supports iPhone only. You can develop and test an app that uses this framework on iPhone in any region. Customer installations of your app can use this framework only on iPhones located in the EU that are signed in with an Apple Account with an EU country or region.

## Topics

### Essentials
- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)
  Enable your accessory to receive forwarded Live Activities by updating your data provider extension.
### Authorization
- [class LiveActivityForwarding](liveactivityforwarding.md)
  A class for requesting permission to forward Live Activities to your accessory and handle them in your accessory’s data provider extension.
- [enum AccessoryAuthorizationResult](accessoryauthorizationresult.md)
  Responses to the Live Activity forwarding permission prompt.
### Live Activity forwarding
- [LiveActivityForwarding.AccessoryLiveActivitiesHandler](liveactivityforwarding/accessoryliveactivitieshandler.md)
  A protocol that defines methods for handling Live Activity life cycle events in your accessory’s data provider extension.
- [LiveActivityForwarding.Session](liveactivityforwarding/session.md)
  An object that represents the active connection between your data provider extension and the system.
### Live Activity data access
- [struct AccessoryLiveActivity](accessoryliveactivity.md)
  The details of the Live Activity that iOS forwards to your accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryLiveActivities)*