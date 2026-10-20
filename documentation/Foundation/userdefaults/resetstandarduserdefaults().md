# resetStandardUserDefaults()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

This method has no effect and shouldn’t be used.

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
class func resetStandardUserDefaults()
```

```objc
+ (void) resetStandardUserDefaults;
```

## See Also

### Deprecated
- [convenience init?(user: String)](./init%28user%29.md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](./synchronize%28%29.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](./persistentdomainnames%28%29.md)
  Returns an array of the current persistent domain names.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](./completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](./didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](./nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](../language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/resetstandarduserdefaults())*