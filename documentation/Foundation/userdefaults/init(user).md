# init(user:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a user defaults object initialized with the defaults for the specified user account.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This method was never implemented to return anything but the defaults for the current user. Use [`standard`](./standard.md) instead.

## Declaration

```swift
convenience init?(user username: String)
```

```objc
- (id) initWithUser:(NSString *) username;
```

#### Return Value

An initialized [`UserDefaults`](../userdefaults.md) object whose argument and registration domains are already set up. If the current user does not have access to the specified user account, this method returns `nil`.

#### Discussion

This method doesn’t put anything in the search list. Invoke it only if you’ve allocated your own [`UserDefaults`](../userdefaults.md) instance instead of using the shared one.

You do not normally use this method to initialize an instance of [`UserDefaults`](../userdefaults.md). Applications used by a superuser might use this method to update the defaults databases for a number of users. The user who started the application must have appropriate access (read, write, or both) to the defaults database of the new user, or this method returns `nil`.

##### Special Considerations

This method was never implemented to do anything except return the defaults for the current user.

## Parameters

- `username`: The name of the user account.

## See Also

### Related Documentation
- [class var standard: UserDefaults](./standard.md)
  The shared defaults object for the current app.
### Deprecated
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
- [class let noCloudAccountNotification: NSNotification.Name](./nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
- [Language-Dependent Information Constants](../language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/init(user:))*