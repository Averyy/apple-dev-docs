# synchronize()

**Framework**: Foundation  
**Kind**: method

Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func synchronize() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data was saved successfully to disk, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the keys and values from the specified persistent domain.
- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Retrieves the settings from the specified persistent domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/synchronize())*