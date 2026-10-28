# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The string that you use internally to identify the action.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIMutableUserNotificationAction`](../uimutableusernotificationaction.md).

## Declaration

```swift
var identifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * identifier;
```

## Discussion

The system passes this string to the [`application(_:handleActionWithIdentifier:for:completionHandler:)`](../uiapplicationdelegate/application%28_,handleactionwithidentifier,for,completionhandler%29.md) or [`application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)`](../uiapplicationdelegate/application%28_,handleactionwithidentifier,forremotenotification,completionhandler%29.md) method of the app delegate when the user chooses the action.

## See Also

### Getting the action information
- [var title: String?](./title.md)
  The localized string to use as the button title for the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/identifier)*