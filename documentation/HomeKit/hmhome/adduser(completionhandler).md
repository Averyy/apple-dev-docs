# addUser(completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a user to the home.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 8.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`manageUsers(completionHandler:)`](./manageusers%28completionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func addUser(completionHandler completion: @escaping @Sendable (HMUser?, (any Error)?) -> Void)
```

*visionOS*

```swift
func addUser() async throws -> HMUser
```

```objc
- (void) addUserWithCompletionHandler:(void (^)(HMUser *user, NSError *error)) completion;
```

## Parameters

- `completion`: The block executed after the request is processed.

  - **user**: The user that was added to the home.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure. `error.userInfo[HMUserFailedAccessoriesKey]` contains more information in case of failure. See [`HMUserFailedAccessoriesKey`](../hmuserfailedaccessorieskey.md) for more details.

## See Also

### Deprecated symbols
- [var users: [HMUser]](./users.md)
  All users associated with the home.
- [func removeUser(HMUser, completionHandler: ((any Error)?) -> Void)](./removeuser%28_,completionhandler%29.md)
  Removes a user from the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/adduser(completionhandler:))*