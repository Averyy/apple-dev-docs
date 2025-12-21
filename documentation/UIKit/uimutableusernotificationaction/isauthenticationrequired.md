# isAuthenticationRequired

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the user must unlock the device before the action is performed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isAuthenticationRequired: Bool { get set }
```

#### Discussion

The value of this property is ignored and treated as a value of [`true`](https://developer.apple.com/documentation/Swift/true) when the value of the [`activationMode`](uimutableusernotificationaction/activationmode.md) property is set to [`UIMutableUserNotificationAction`](uimutableusernotificationaction.md).

If your app uses data protection to encrypt data on disk, consider the data needs of the corresponding action before setting this property to [`false`](https://developer.apple.com/documentation/Swift/false). For many data protection classes, data remains encrypted and unavailable while the device is locked. If your app needs to access encrypted data to perform a task, you likely need to set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to ensure that the data is accessible.

## See Also

- [var activationMode: UIUserNotificationActivationMode](uimutableusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isDestructive: Bool](uimutableusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](uimutableusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](uimutableusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/isauthenticationrequired)*