# Notifications.NotificationSettingsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The notification settings dictionary.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.15+

## Declaration

```
object Notifications.NotificationSettingsItem
```

## Properties

- `AlertType` (integer): The type of alert for notifications for this app:

  - `0`: None
  - `1`: Temporary Banner
  - `2`: Persistent Banner

  **Default**: `1`; **Allowed Values**: `0`, `1`, `2`
- `BadgesEnabled` (boolean): If `true`, enables badges for this app.

  **Default**: `true`
- `BundleIdentifier` (string) *(required)*: The bundle identifier of the app to which to apply these notification settings.
- `CriticalAlertEnabled` (boolean): If `true`, enables critical alerts that can ignore Do Not Disturb and ringer settings for this app.

  Available: iOS 12+ | iPadOS 12+ | macOS 10.15+

  **Default**: `false`
- `GroupingType` (integer): The type of grouping for notifications for this app:

  - `0`: Automatic: Group notifications into app-specified groups.
  - `1`: By app: Group notifications into one group.
  - `2`: Off: Don’t group notifications.

  Available: iOS 12+ | iPadOS 12+

  **Default**: `0`; **Allowed Values**: `0`, `1`, `2`
- `NotificationsEnabled` (boolean): If `true`, enables notifications for this app.

  **Default**: `true`
- `PreviewType` (integer): The type previews for notifications. This key overrides the value at Settings>Notifications>Show Previews.

  - `0` - Always: The device shows previews when locked and unlocked
  - `1` - When Unlocked: The device shows previews only when unlocked
  - `2` - Never: The device never shows previews

  Available: iOS 14+ | iPadOS 14+

  **Allowed Values**: `0`, `1`, `2`
- `ShowInCarPlay` (boolean): If `true`, enables notifications in CarPlay for this app.

  Available: iOS 12+ | iPadOS 12+

  **Default**: `true`
- `ShowInLockScreen` (boolean): If `true`, enables notifications on the Lock Screen for this app.

  **Default**: `true`
- `ShowInNotificationCenter` (boolean): If `true`, enables notifications in the Notification Center for this app.

  **Default**: `true`
- `SoundsEnabled` (boolean): If `true`, enables sounds for this app.

  **Default**: `true`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/notifications/notificationsettingsitem)*