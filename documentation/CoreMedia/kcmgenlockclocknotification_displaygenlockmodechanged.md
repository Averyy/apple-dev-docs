# kCMGenlockClockNotification_DisplayGenlockModeChanged

**Framework**: Core Media  
**Kind**: var

Posted when the display mode changes from genlock to non-genlock or vice versa.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let kCMGenlockClockNotification_DisplayGenlockModeChanged: CFString
```

#### Discussion

Observe this notification using `CMNotificationCenterAddListener` on the default local `CMNotificationCenter`. The notification payload dictionary contains a `CFBoolean` value for the key `kCMGenlockClockNotificationPayload_AnyDisplayIsSynchronizedToLockedGenlockSignal`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmgenlockclocknotification_displaygenlockmodechanged)*