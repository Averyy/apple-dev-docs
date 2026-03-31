# AccessoryAuthorizationResult

**Framework**: Accessory Live Activities  
**Kind**: enum

Responses to the Live Activity forwarding permission prompt.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
enum AccessoryAuthorizationResult
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Call [`authorization(forAccessory:)`](liveactivityforwarding/authorization(foraccessory:).md) to check the current forwarding authorization for an accessory without showing any UI. If the result is `.undetermined`, ask people for their permission to forward iOS system notifications and Live Activities to your accessory. For more information, see [`Receiving Live Activity updates and alerts on an accessory`](receiving-live-activities-on-an-accessory.md).

To ask if someone wants to update their current selection – for example, if they previously denied Live Activity forwarding – call [`presentAuthorizationSheet(forAccessory:)`](liveactivityforwarding/presentauthorizationsheet(foraccessory:).md).

## Topics

### Identifying the decision
- [AccessoryAuthorizationResult.undetermined](accessoryauthorizationresult/undetermined.md)
  An option that indicates the system hasn’t shown the authorization prompt to the person.
- [AccessoryAuthorizationResult.allow](accessoryauthorizationresult/allow.md)
  An option that indicates the person allows Live Activity forwarding from all apps that support them.
- [AccessoryAuthorizationResult.limited](accessoryauthorizationresult/limited.md)
  An option that indicates the person allows Live Activities from a selected subset of apps.
- [AccessoryAuthorizationResult.deny](accessoryauthorizationresult/deny.md)
  An option that indicates the person doesn’t allow Live Activities.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LiveActivityForwarding](liveactivityforwarding.md)
  A class for requesting permission to forward Live Activities to your accessory and handle them in your accessory’s data provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryauthorizationresult)*