# ACAccountStoreDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the accounts managed by this account store changed in the database.

**Availability**:
- iOS 5.0+ - Deprecated in 14.0
- iPadOS 5.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: Public notification deprecated. Internal clients, see private header for replacement

## Declaration

```swift
static let ACAccountStoreDidChange: NSNotification.Name
```

#### Discussion

The notification sent if an account is saved or removed locally or externally. If you receive this notification, you should refetch all account objects.

There’s no `userInfo` dictionary associated with this notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/acaccountstoredidchange)*