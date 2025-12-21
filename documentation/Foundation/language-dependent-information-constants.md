# Language-Dependent Information Constants

**Framework**: Foundation

These constants are deprecated and shouldn’t be used.

## See Also

- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](userdefaults/synchronize.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/language-dependent-information-constants)*