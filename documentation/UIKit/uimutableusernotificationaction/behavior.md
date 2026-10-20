# behavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The custom behavior (if any) that the action supports.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var behavior: UIUserNotificationActionBehavior { get set }
```

```objc
@property (nonatomic, assign) UIUserNotificationActionBehavior behavior;
```

#### Discussion

The default value of this property is `UIUserNotificationActionBehaviorDefault`.

## See Also

### Configuring the action’s behavior
- [var activationMode: UIUserNotificationActivationMode](./activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](./isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](./isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var parameters: [AnyHashable : Any]](./parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/behavior)*