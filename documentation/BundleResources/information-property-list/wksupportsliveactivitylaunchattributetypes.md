# WKSupportsLiveActivityLaunchAttributeTypes

**Framework**: Bundle Resources  
**Kind**: typealias

The attribute type names that let a person launch your watchOS app by tapping a Live Activity.

**Availability**:
- watchOS 11.1+



**Type**: string

#### Discussion

When your iOS app starts a Live Activity, the system can forward it to an Apple Watch that has a paired watchOS app installed. If the person taps the Live Activity in the Smart Stack, the system checks whether your watchOS app declares a matching attribute type in this key. If the Live Activity’s attribute type matches an entry, the system launches the watchOS app and identifies that Live Activity as the reason for the launch.

If no matching entry exists, or if no watchOS app is installed, the system instead shows a full-screen wrapper around the Live Activity with an option to open the app on iPhone.

This key corresponds to the `Supports Launch for Live Activity Attribute Types` build setting for your watchOS app target. If you manage your `Info.plist` file manually, add this key directly. If you use `GENERATE_INFOPLIST_FILE`, set the `INFOPLIST_KEY_WKSupportsLiveActivityLaunchAttributeTypes` build setting instead and Xcode writes the key for you. To support launch for all of your Live Activities, leave the array empty. To restrict launch to specific Live Activities, add one entry per [`ActivityAttributes`](https://developer.apple.com/documentation/ActivityKit/ActivityAttributes)-conforming type that initiates a launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wksupportsliveactivitylaunchattributetypes)*