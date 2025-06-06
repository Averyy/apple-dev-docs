# removeUser(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a user from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeUser(_ user: HMUser) async throws
```

## Parameters

- `user`: The user to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var users: [HMUser]](hmhome/users.md)
  All users associated with the home.
- [func addUser(completionHandler: (HMUser?, (any Error)?) -> Void)](hmhome/adduser(completionhandler:).md)
  Adds a user to the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeuser(_:completionhandler:))*