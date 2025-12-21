# completedInitialCloudSyncNotification

**Framework**: Foundation  
**Kind**: property

Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let completedInitialCloudSyncNotification: NSNotification.Name
```

#### Discussion

This notification is posted on the main queue.

## See Also

- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](userdefaults/synchronize.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/completedinitialcloudsyncnotification)*