# users

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

All users associated with the home.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 8.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var users: [HMUser] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMUser *> * users;
```

## See Also

### Deprecated symbols
- [func addUser(completionHandler: (HMUser?, (any Error)?) -> Void)](./adduser%28completionhandler%29.md)
  Adds a user to the home.
- [func removeUser(HMUser, completionHandler: ((any Error)?) -> Void)](./removeuser%28_,completionhandler%29.md)
  Removes a user from the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/users)*