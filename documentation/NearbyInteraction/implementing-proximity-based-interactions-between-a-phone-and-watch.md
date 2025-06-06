# Implementing proximity-based interactions between a phone and watch

**Framework**: Nearbyinteraction

Interact with a nearby Apple Watch by measuring its distance to a paired iPhone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- watchOS 8.0+
- Xcode 13.3+

#### Overview

> **Note**: This sample code project is associated with WWDC21 session [`10165: Explore Nearby Interaction with Third-Party Accessories`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10165).

##### Configure the Sample Code Project

You can run this sample either in the simulator or on paired devices. When running on paired devices, both the watch and iPhone must contain the U1 chip.

To run on paired devices:

1. Select the WatchNIDemo target, then change the bundle ID to `<Your iOS app bundle ID>`. Select the right team to let Xcode automatically manage your provisioning profile.
2. Repeat step 1 for the WatchKit app and WatchKit Extension target. The bundle IDs should be `<Your iOS app bundle ID>.watchkitapp` and `<Your iOS app bundle ID>.watchkitapp.watchkitextension` respectively.
3. Next, for the WatchKit app target, select the Info tab, and change the value of `WKCompanionAppBundleIdentifier` key to `<Your iOS app bundle ID>`.
4. Finally, open the `Info.plist` file of the WatchKit Extension target, navigate to `NSExtension` > `NSExtensionAttributes` > `WKAppBundleIdentifier` key, and change the value of the key to `<Your iOS app bundle ID>.watchkitapp`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NearbyInteraction/implementing-proximity-based-interactions-between-a-phone-and-watch)*