# removeNotifications(forIdentifiers:sourceIdentifier:for:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Removes notifications posted by an application.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func removeNotifications(forIdentifiers identifiers: Set<String>, sourceIdentifier: String, for accessory: ASAccessory) async throws
```

#### Discussion

This method has equivalent behavior to clearing notifications from Notification Center on the phone. The method only throws errors related to receiving the request; it doesn’t throw errors if some identifiers can’t be cleared because the notifications were already removed.

## Parameters

- `identifiers`: A set of identifiers for each notification to clear.
- `sourceIdentifier`: The bundle identifier of the app that posted the notifications.
- `accessory`: The accessory that is clearing notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationmanaging/removenotifications(foridentifiers:sourceidentifier:for:))*