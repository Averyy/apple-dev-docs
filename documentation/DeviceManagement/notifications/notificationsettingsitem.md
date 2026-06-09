# Notifications.NotificationSettingsItem

**Framework**: Device Management  
**Kind**: dictionary

The notification settings dictionary.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.15+

## Declaration

```swift
object Notifications.NotificationSettingsItem
```

## Properties

- `AlertType` (integer): The type of alert for notifications for this app: - `0`: None
- `1`: Temporary Banner
- `2`: Persistent Banner
- `BadgesEnabled` (boolean): If `true`, enables badges for this app.
- `BundleIdentifier` (string) *(required)*: The bundle identifier of the app to which to apply these notification settings.
- `CriticalAlertEnabled` (boolean): If `true`, enables critical alerts that can ignore Do Not Disturb and ringer settings for this app. Available: iOS 12+ | iPadOS 12+ | macOS 10.15+
- `GroupingType` (integer): The type of grouping for notifications for this app: - `0`: Automatic: Group notifications into app-specified groups.
- `1`: By app: Group notifications into one group.
- `2`: Off: Don’t group notifications. Available: iOS 12+ | iPadOS 12+
- `NotificationsEnabled` (boolean): If `true`, enables notifications for this app.
- `PreviewType` (integer): The type previews for notifications. This key overrides the value at Settings>Notifications>Show Previews. - `0` - Always: Previews will be shown when the device is locked and unlocked
- `1` - When Unlocked: Previews will only be shown when the device is unlocked
- `2` - Never: Previews will never be shown Available: iOS 14+ | iPadOS 14+
- `ShowInCarPlay` (boolean): If `true`, enables notifications in CarPlay for this app. Available: iOS 12+ | iPadOS 12+
- `ShowInLockScreen` (boolean): If `true`, enables notifications on the Lock Screen for this app.
- `ShowInNotificationCenter` (boolean): If `true`, enables notifications in the notification center for this app.
- `SoundsEnabled` (boolean): If `true`, enables sounds for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/notifications/notificationsettingsitem)*