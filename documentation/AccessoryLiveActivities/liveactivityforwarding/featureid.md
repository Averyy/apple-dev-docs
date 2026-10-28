# featureID

**Framework**: Accessory Live Activities  
**Kind**: property  
**Role**: Type Property

A constant you use to configure your data provider extension’s capability to forward Live Activities to your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static let featureID: String
```

## Overview

This constant’s value is `AccessoryLiveActivities.LiveActivityForwarding`, the string you add to your data provider extension to configure the capability to receive forwarded Live Activities.

## See Also

### Requesting Live Activity forwarding
- [init(() -> any LiveActivityForwarding.AccessoryLiveActivitiesHandler)](./init%28_%29.md)
  Creates an object you use to manage Live Activity forwarding for your accessory.
- [static func authorization(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](./authorization%28foraccessory%29.md)
  Checks whether someone permits the system to forward Live Activities to the given accessory.
- [static func presentAuthorizationSheet(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](./presentauthorizationsheet%28foraccessory%29.md)
  Presents the system UI that allows people to manage their permission to forward Live Activities to an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/featureid)*