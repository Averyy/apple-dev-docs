# noCloudAccountNotification

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when a cloud default is set, but no iCloud user is logged in.

**Availability**:
- iOS 9.3+ - Deprecated in 9.3
- iPadOS 9.3+ - Deprecated in 9.3
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Notification is never posted

## Declaration

```swift
class let noCloudAccountNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSUbiquitousUserDefaultsNoCloudAccountNotification;
```

## Discussion

This notification is posted to the default notification center on the main queue.

This notification doesn’t necessarily indicate an error; ubiquitous defaults set when no iCloud user is logged in are uploaded the next time one is available if configured to do so.

## See Also

### Deprecated
- [convenience init?(user: String)](./init%28user%29.md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](./synchronize%28%29.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](./resetstandarduserdefaults%28%29.md)
  This method has no effect and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](./persistentdomainnames%28%29.md)
  Returns an array of the current persistent domain names.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](./completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](./didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [Language-Dependent Information Constants](../language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/nocloudaccountnotification)*