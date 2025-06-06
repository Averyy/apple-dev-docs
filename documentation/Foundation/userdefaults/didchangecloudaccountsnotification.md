# didChangeCloudAccountsNotification

**Framework**: Foundation  
**Kind**: property

Posted when the user changes the primary iCloud account.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let didChangeCloudAccountsNotification: NSNotification.Name
```

#### Discussion

This notification is posted to the default notification center on the main queue.The keys and values in the local key-value store are replaced with those from the new account, regardless of the relative timestamps.

## See Also

- [class let didChangeNotification: NSNotification.Name](userdefaults/didchangenotification.md)
  Posted when user defaults are changed within the current process.
- [class let sizeLimitExceededNotification: NSNotification.Name](userdefaults/sizelimitexceedednotification.md)
  Posted when more data is stored in user defaults than is allowed.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/didchangecloudaccountsnotification)*