# currentUser

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The current HomeKit user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentUser: HMUser { get }
```

```objc
@property (nonatomic, strong, readonly) HMUser * currentUser;
```

## See Also

### Managing users
- [func manageUsers(completionHandler: ((any Error)?) -> Void)](./manageusers%28completionhandler%29.md)
  Presents a view controller to manage users of the home.
- [class HMUser](../hmuser.md)
  A person in the home who may have access to control accessories and services in the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/currentuser)*