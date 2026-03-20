# complete(didAlert:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Notifies the system of whether your accessory successfully alerted the person for the notification.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func complete(didAlert: Bool)
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

## Parameters

- `didAlert`: A Boolean value that indicates whether the accessory alerted the person. Pass `true` if the accessory alerted; otherwise, `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertcoordinating/complete(didalert:))*