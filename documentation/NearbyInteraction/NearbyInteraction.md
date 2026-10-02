# Nearby Interaction

**Framework**: Nearby Interaction  
**Kind**: module

Locate and interact with nearby devices using identifiers, distance, and direction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 8.0+

#### Overview

Use Nearby Interaction in your app to acquire the position of devices with an Ultra Wideband (UWB) chip, such as iPhone 11 or later, Apple Watch, and third-party accessories. To participate in an interaction, devices in physical proximity run an app and share their position and device tokens that uniquely identify them. When the app runs in the foreground, Nearby Interaction notifies the interaction session of the peer’s location by reporting the peer’s direction and distance in meters.

Apple devices use the high-frequency capabilities of the UWB chip to share their positions in the physical environment and enable fluid, interactive sessions. For example:

- A multiuser AR experience that places virtual water balloons in the hands of its participants
- A taxi or rideshare app that employs a peer user’s direction in real time to identify the relative locations of a driver and a customer
- A game app that enables a user to control a paddle with their device and respond to a moving ball on the peer user’s screen, as in the following figure

![An illustration of two hands, each holding an iPhone. Arrows extend from the phones to indicate the users’ physical movement. Onscreen, the app displays a ball and paddle game where the first user’s movement slides the bottom paddle left or right, and the opponent’s movement slides the top paddle left or right. In the center of the screen, a ball with motion lines indicates the movement of the ball as it bounces off the first user’s paddle and heads to the upper-right corner of the screen, which isn’t guarded by the opponent’s paddle. ](/images/com.apple.nearbyinteraction/media-3880159@2x.png)

For guidance on designing nearby interactions, see the [`Human Interface Guidelines > Nearby interactions`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/nearby-interactions).

##### Interact with Apple Watch

The UWB chip-capable Apple Watch running watchOS 8 supports Nearby Interaction sessions. Apps share discovery tokens to begin an interaction session in watchOS using a custom server, [`Core Bluetooth`](https://developer.apple.com/documentation/corebluetooth), LAN (TCP/UDP), or [`Watch Connectivity`](https://developer.apple.com/documentation/watchconnectivity).

Nearby Interaction in iOS provides a peer device’s distance and direction, whereas Nearby Interaction in watchOS provides only a peer device’s distance.

##### Interact with Third Party Devices

In iOS 15 and later and watchOS 8 and later, UWB-enabled devices can interact with third-party accessories you partner with or develop using the [`Nearby Interaction Accessory Protocol Specification`](https://developer.apple.comhttps://developer.apple.com/nearby-interaction/specification). To begin an interaction session with a third-party accessory, establish a data link with the accessory, receive its configuration data, and create an [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md). The framework provides configuration data for your device through [`session(_:didGenerateShareableConfigurationData:for:)`](nisessiondelegate/session(_:didgenerateshareableconfigurationdata:for:).md) that your app sends to the accessory to begin detecting the accessory’s range. For more information on accessory interaction, see [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md).

> **Note**:  The [`supportsPreciseDistanceMeasurement`](nidevicecapability/supportsprecisedistancemeasurement.md) function returns [`false`](https://developer.apple.com/documentation/swift/false) in Mac apps built with Mac Catalyst. For a compatible iPad or iPhone app running in visionOS, framework features are unavailable, and any calls you make to the framework APIs have no effect.

##### Using Nearby Interaction in the Background

While your app is in the foreground, it can freely use Nearby Interaction to range with a peer device or third-party accessory. When the app moves to the background, it can continue ranging only if the peer or accessory is Bluetooth Low Energy (LE)-paired and connected.

In iOS 18.4 and later, your app can continue ranging in the background with any supported peer or accessory if the app starts a Live Activity as it goes to the background. For more information about creating Live Activities, see [`ActivityKit`](https://developer.apple.com/documentation/activitykit).

In iOS 27.2 and later, DL-TDOA sessions can begin when the system relaunches your app in the background. For example, if your app uses iBeacon region monitoring and DL-TDOA together to locate a device in the physical environment, you can start the DL-TDOA session immediately in the iBeacon region-entry callback. For more information, see [`Downlink time difference of arrival ranging`](dl-tdoa-ranging.md).

> **Note**: Enable a capability in Xcode for the  type of background activity your app uses. In your target’s Signing & Capabilities tab, add the Background Modes capability, then select Uses Nearby Interaction.

##### Setup

- [`Initiating and maintaining a session`](initiating-and-maintaining-a-session.md)
- [`NISession`](nisession.md)

##### Authorization

- [`NSNearbyInteractionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionusagedescription)

##### Phone Interaction

- [`Implementing interactions between users in close proximity`](implementing-interactions-between-users-in-close-proximity.md)
- [`Discovering peers with Multipeer Connectivity`](discovering-peers-with-multipeer-connectivity.md)
- [`Extending advanced direction finding and ranging`](extending-advanced-direction-finding-and-ranging.md)
- [`NINearbyPeerConfiguration`](ninearbypeerconfiguration.md)

##### Watch Interaction

- [`Implementing proximity-based interactions between a phone and watch`](implementing-proximity-based-interactions-between-a-phone-and-watch.md)

##### Third Party Accessories

- [`Implementing spatial interactions with third-party accessories`](implementing-spatial-interactions-with-third-party-accessories.md)
- [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md)
- [`NIMotionActivityState`](nimotionactivitystate.md)

##### Periodic Updates

- [`NINearbyObject`](ninearbyobject.md)
- [`NISessionDelegate`](nisessiondelegate.md)

##### Camera Assistance

- [`Finding devices with precision`](finding-devices-with-precision.md)
- [`NIAlgorithmConvergence`](nialgorithmconvergence.md)
- [`NIAlgorithmConvergenceStatus`](nialgorithmconvergencestatus-2fnve.md)
- [`NIAlgorithmConvergenceStatus`](nialgorithmconvergencestatus-2fbmj.md)
- [`Algorithm Convergence Status`](algorithm-convergence-status.md)

##### Dl Tdoa Ranging

- [`Downlink time difference of arrival ranging`](dl-tdoa-ranging.md)

##### Errors

- [`NIError`](nierror.md)
- [`NIError.Code`](nierror/code.md)
- [`NIErrorDomain`](nierrordomain.md)

##### Deprecated

Avoid using deprecated configuration in your apps.

- [`NSNearbyInteractionAllowOnceUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionallowonceusagedescription)

## Topics

### Articles
- [Algorithm Convergence Status](algorithm-convergence-status.md)
  The possible Objective-C states of Camera Assistance.
- [Discovering peers with Multipeer Connectivity](discovering-peers-with-multipeer-connectivity.md)
  Exchange discovery tokens over the local network.
- [Downlink time difference of arrival ranging](dl-tdoa-ranging.md)
  Use anchor devices to improve the accuracy of indoor positioning.
- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)
  Extend your app’s direction finding capabilities with data from Ultra Wideband devices.
- [Finding devices with precision](finding-devices-with-precision.md)
  Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device.
- [Implementing interactions between users in close proximity](implementing-interactions-between-users-in-close-proximity.md)
  Enable devices to access relative positioning information.
- [Implementing proximity-based interactions between a phone and watch](implementing-proximity-based-interactions-between-a-phone-and-watch.md)
  Interact with a nearby Apple Watch by measuring its distance to a paired iPhone.
- [Implementing spatial interactions with third-party accessories](implementing-spatial-interactions-with-third-party-accessories.md)
  Establish a connection with a nearby accessory to receive periodic measurements of its distance from the user.
- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)
  Measure the relative position of a nearby device and coach the user to sustain interaction.
### Classes
- [class NIAlgorithmConvergence](nialgorithmconvergence.md)
  An object that provides the state and reason for user coaching recommendations.
- [class NINearbyAccessoryConfiguration](ninearbyaccessoryconfiguration.md)
  A configuration that enables interaction between iPhone and third-party accessories.
- [class NINearbyObject](ninearbyobject.md)
  Location information for a peer device in an interaction session.
- [class NINearbyPeerConfiguration](ninearbypeerconfiguration.md)
  A configuration that enables interaction between iPhone or Apple Watch devices.
- [class NISession](nisession.md)
  An object that identifies a unique connection between two peer devices.
### Protocols
- [protocol NISessionDelegate](nisessiondelegate.md)
  An object that monitors and reacts to session updates.
### Structures
- [struct NIError](nierror.md)
  An error Nearby Interaction reports.
### Variables
- [let NIErrorDomain: String](nierrordomain.md)
  A unique error domain for Nearby Interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NearbyInteraction)*