# NSNearbyInteractionUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A request for user permission to begin an interaction session with nearby devices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- watchOS 8.0+

#### Discussion

This property defines localizable text that explains your interaction session’s purpose to the user.

Before an app starts an interaction session, the system checks whether the user agrees to share their relative distance and direction with a nearby peer. The first time the app runs, the framework presents a prompt that displays the value of this key contained in your project’s `Info.plist`. The system persists the user’s choice in Settings. After your app runs for the first time, it consults the user preference in Settings before it begins a new interaction session.

For more information, see [`Initiating and maintaining a session`](https://developer.apple.com/documentation/NearbyInteraction/initiating-and-maintaining-a-session).

## See Also

- [NSLocalNetworkUsageDescription](information-property-list/nslocalnetworkusagedescription.md)
  A message that tells the user why the app is requesting access to the local network.
- [NSNearbyInteractionAllowOnceUsageDescription](information-property-list/nsnearbyinteractionallowonceusagedescription.md)
  A one-time request for user permission to begin an interaction session with nearby devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionusagedescription)*