# addUser(completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a user to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func addUser() async throws -> HMUser
```

## Parameters

- `completion`: The block executed after the request is processed.

## See Also

- [var users: [HMUser]](hmhome/users.md)
  All users associated with the home.
- [func removeUser(HMUser, completionHandler: ((any Error)?) -> Void)](hmhome/removeuser(_:completionhandler:).md)
  Removes a user from the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/adduser(completionhandler:))*