# NSNearbyInteractionAllowOnceUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A one-time request for user permission to begin an interaction session with nearby devices.

**Availability**:
- iOS 14.0+ - Deprecated in 15.0
- iPadOS 14.0+ - Deprecated in 15.0

## Details

- **Name**: `NSNearbyInteractionAllowOnceUsageDescription` (Privacy - Nearby Interaction Allow Once Usage Description)
- **Type**: string

#### Discussion

> ⚠️ **Warning**:  Define this property in the `Info.plist` only for apps that deploy to iOS 14. [`NSNearbyInteractionUsageDescription`](./nsnearbyinteractionusagedescription.md) replaces this property in iOS 15 and later.

Before an app starts an interaction session, the system requests permission to share the user’s relative distance and direction with a nearby peer. The framework presents a prompt that displays the value of this key contained in your project’s `Info.plist`. Define text that explains your interaction session’s purpose to the user. For more information, see [Initiating and maintaining a session](../../NearbyInteraction/initiating-and-maintaining-a-session.md).

## See Also

### Networking
- [NSLocalNetworkUsageDescription](./nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [NSNearbyInteractionUsageDescription](./nsnearbyinteractionusagedescription.md)
  A request for user permission to begin an interaction session with nearby devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionallowonceusagedescription)*