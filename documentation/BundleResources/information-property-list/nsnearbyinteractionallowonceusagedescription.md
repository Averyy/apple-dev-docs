# NSNearbyInteractionAllowOnceUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A one-time request for user permission to begin an interaction session with nearby devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

> ⚠️ **Warning**:  Define this property in the `Info.plist` only for apps that deploy to iOS 14. [`NSNearbyInteractionUsageDescription`](information-property-list/nsnearbyinteractionusagedescription.md) replaces this property in iOS 15 and later.

Before an app starts an interaction session, the system requests permission to share the user’s relative distance and direction with a nearby peer. The framework presents a prompt that displays the value of this key contained in your project’s `Info.plist`. Define text that explains your interaction session’s purpose to the user. For more information, see [`Initiating and maintaining a session`](https://developer.apple.com/documentation/NearbyInteraction/initiating-and-maintaining-a-session).

## See Also

- [NSLocalNetworkUsageDescription](information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [NSNearbyInteractionUsageDescription](information-property-list/nsnearbyinteractionusagedescription.md)
  A request for user permission to begin an interaction session with nearby devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionallowonceusagedescription)*