# removeUser(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a user from the home.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`manageUsers(completionHandler:)`](./manageusers%28completionhandler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func removeUser(_ user: HMUser, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

*Mac Catalyst, visionOS*

```swift
func removeUser(_ user: HMUser) async throws
```

```objc
- (void) removeUser:(HMUser *) user completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `user`: The user to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure. `error.userInfo[HMUserFailedAccessoriesKey]` contains more information in case of failure. See [`HMUserFailedAccessoriesKey`](../hmuserfailedaccessorieskey.md) for more details.

## See Also

### Deprecated symbols
- [var users: [HMUser]](./users.md)
  All users associated with the home.
- [func addUser(completionHandler: (HMUser?, (any Error)?) -> Void)](./adduser%28completionhandler%29.md)
  Adds a user to the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeuser(_:completionhandler:))*