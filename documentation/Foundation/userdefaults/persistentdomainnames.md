# persistentDomainNames()

**Framework**: Foundation  
**Kind**: method

Returns an array of the current persistent domain names.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func persistentDomainNames() -> [Any]
```

#### Return Value

An array of `NSString` objects containing the domain names.

#### Discussion

You can get the keys and values for each domain by passing the returned domain names to the  [`persistentDomain(forName:)`](userdefaults/persistentdomain(forname:).md) method.

## See Also

- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](userdefaults/synchronize.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/persistentdomainnames())*