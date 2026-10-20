# isAuthenticationRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user must unlock the device before the action is performed.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIMutableUserNotificationAction`](../uimutableusernotificationaction.md).

## Declaration

```swift
var isAuthenticationRequired: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isAuthenticationRequired) BOOL authenticationRequired;
```

#### Discussion

The value of this property is ignored and treated as a value of [`true`](../../Swift/true.md) when the value of the [`activationMode`](./activationmode.md) property is set to [`UIMutableUserNotificationAction`](../uimutableusernotificationaction.md).

If your app uses data protection to encrypt data on disk, consider the data needs of the corresponding action before setting this property to [`false`](../../Swift/false.md). For many data protection classes, data remains encrypted and unavailable while the device is locked. If your app needs to access encrypted data to perform a task, you likely need to set this property to [`true`](../../Swift/true.md) to ensure that the data is accessible.

## See Also

### Configuring the action’s behavior
- [var activationMode: UIUserNotificationActivationMode](./activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isDestructive: Bool](./isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](./behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](./parameters.md)
  A dictionary of additional parameters to include with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/isauthenticationrequired)*