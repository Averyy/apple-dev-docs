# persistentDomainNames()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of the current persistent domain names.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Instead of using this method, you should track the domains you add if you want to later retrieve them with [`persistentDomain(forName:)`](./persistentdomain%28forname%29.md).

## Declaration

```swift
func persistentDomainNames() -> [Any]
```

```objc
- (NSArray *) persistentDomainNames;
```

## Return Value

An array of `NSString` objects containing the domain names.

## Discussion

You can get the keys and values for each domain by passing the returned domain names to the  [`persistentDomain(forName:)`](./persistentdomain%28forname%29.md) method.

## See Also

### Deprecated
- [convenience init?(user: String)](./init%28user%29.md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](./synchronize%28%29.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](./resetstandarduserdefaults%28%29.md)
  This method has no effect and shouldn’t be used.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](./completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](./didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](./nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](../language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/persistentdomainnames())*