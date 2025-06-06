# SCPreferencesCallBack

**Framework**: System Configuration  
**Kind**: typealias

Type of the callback function used when the preferences have been updated or applied.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias SCPreferencesCallBack = (SCPreferences, SCPreferencesNotification, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `prefs`: The preferences session.
- `notificationType`: The type of notification, such as changes committed or changes applied. See   for information about possible values.
- `info`: A C pointer to a user-specified block of data.

## Topics

### Fields
- [prefs](1808420-prefs.md)
  The preferences session.
- [notificationType](1808421-notificationtype.md)
  The type of notification, such as changes committed or changes applied. See [`SCPreferencesNotification`](scpreferencesnotification.md) for information about possible values.

## See Also

- [class SCPreferences](scpreferences.md)
  The handle to an open preferences session for accessing system configuration preferences.
- [struct SCPreferencesContext](scpreferencescontext.md)
  A structure containing user-specified data and callbacks for accessing system configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescallback)*