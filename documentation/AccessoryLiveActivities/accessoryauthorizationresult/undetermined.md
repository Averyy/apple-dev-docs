# AccessoryAuthorizationResult.undetermined

**Framework**: Accessory Live Activities  
**Kind**: case

An option that indicates the system hasn’t shown the authorization prompt to the person.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
case undetermined
```

#### Discussion

An `.undetermined` authorization result indicates that the person hasn’t seen the authorization prompt that asks for permission to forward iOS system notifications and Live Activities to your accessory. If they see the authorization prompt and dismiss it, the [`AccessoryAuthorizationResult`](accessoryauthorizationresult.md) changes to [`AccessoryAuthorizationResult.deny`](accessoryauthorizationresult/deny.md).

For more information requesting permission to forward Live Activities to your accessory, see [`Receiving Live Activity updates and alerts on an accessory`](receiving-live-activities-on-an-accessory.md).

## See Also

- [AccessoryAuthorizationResult.allow](accessoryauthorizationresult/allow.md)
  An option that indicates the person allows Live Activity forwarding from all apps that support them.
- [AccessoryAuthorizationResult.limited](accessoryauthorizationresult/limited.md)
  An option that indicates the person allows Live Activities from a selected subset of apps.
- [AccessoryAuthorizationResult.deny](accessoryauthorizationresult/deny.md)
  An option that indicates the person doesn’t allow Live Activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryauthorizationresult/undetermined)*