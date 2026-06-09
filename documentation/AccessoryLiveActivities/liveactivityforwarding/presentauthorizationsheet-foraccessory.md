# presentAuthorizationSheet(forAccessory:)

**Framework**: Accessory Live Activities  
**Kind**: method

Presents the system UI that allows people to manage their permission to forward Live Activities to an accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
static func presentAuthorizationSheet(forAccessory accessory: ASAccessory) async throws -> AccessoryAuthorizationResult
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Return Value

The updated authorization decision.

#### Overview

Call `presentAuthorizationSheet(forAccessory:)` to update which apps forward Live Activities to the accessory after a person has initially responded to the system UI that allows them to authorize forwarded iOS system notifications and Live Activities. The system ignores your call of `presentAuthorizationSheet(forAccessory:)` if you haven’t previously asked someone if they want to receive iOS system notifications and Live Activities on the accessory. For more information about asking for a person’s initial permission, see [`Receiving Live Activity updates and alerts on an accessory`](receiving-live-activities-on-an-accessory.md).

## Parameters

- `accessory`: The accessory that has the authorization settings you want to update.

## See Also

- [init(() -> any LiveActivityForwarding.AccessoryLiveActivitiesHandler)](liveactivityforwarding/init(_:).md)
  Creates an object you use to manage Live Activity forwarding for your accessory.
- [static func authorization(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](liveactivityforwarding/authorization(foraccessory:).md)
  Checks whether someone permits the system to forward Live Activities to the given accessory.
- [static let featureID: String](liveactivityforwarding/featureid.md)
  A constant you use to configure your data provider extension’s capability to forward Live Activities to your accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/presentauthorizationsheet(foraccessory:))*