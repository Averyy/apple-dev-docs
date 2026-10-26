# ACAccountStoreDidChangeNotification

**Framework**: Accounts  
**Kind**: var  
**Role**: Global Variable

Posted when the accounts managed by this account store changed in the database.

**Availability**:
- iOS 5.0+ - Deprecated in 14.0
- iPadOS 5.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0

## Declaration

```c
extern NSString * const ACAccountStoreDidChangeNotification;
```

#### Discussion

The notification sent if an account is saved or removed locally or externally. If you receive this notification, you should refetch all account objects.

There’s no `userInfo` dictionary associated with this notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstoredidchangenotification)*