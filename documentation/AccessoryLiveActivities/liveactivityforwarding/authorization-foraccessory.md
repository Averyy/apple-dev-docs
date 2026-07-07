# authorization(forAccessory:)

**Framework**: Accessory Live Activities  
**Kind**: method

Checks whether someone permits the system to forward Live Activities to the given accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static func authorization(forAccessory accessory: ASAccessory) async throws -> AccessoryAuthorizationResult
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Return Value

The person’s authorization decision for the accessory.

#### Overview

To determine whether someone permits forwarding Live Activities, call `authorization(forAccessory:)` before configuring your accessory or presenting an interface that relates to Live Activity forwarding.

If you want to ask someone to update their authorization – if they denied or limited Live Activity forwarding – present the system UI that allows people to manage their permission to forward Live Activities by calling [`presentAuthorizationSheet(forAccessory:)`](liveactivityforwarding/presentauthorizationsheet(foraccessory:).md).

If the result of the query is [`AccessoryAuthorizationResult.undetermined`](accessoryauthorizationresult/undetermined.md), the system hasn’t presented the authorization UI to the person. For more information about asking for permission for the first time, see [`Receiving Live Activity updates and alerts on an accessory`](receiving-live-activities-on-an-accessory.md).

## Parameters

- `accessory`: The accessory for which to check authorization to forward Live Activities.

## See Also

- [init(() -> any LiveActivityForwarding.AccessoryLiveActivitiesHandler)](liveactivityforwarding/init(_:).md)
  Creates an object you use to manage Live Activity forwarding for your accessory.
- [static func presentAuthorizationSheet(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](liveactivityforwarding/presentauthorizationsheet(foraccessory:).md)
  Presents the system UI that allows people to manage their permission to forward Live Activities to an accessory.
- [static let featureID: String](liveactivityforwarding/featureid.md)
  A constant you use to configure your data provider extension’s capability to forward Live Activities to your accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/authorization(foraccessory:))*