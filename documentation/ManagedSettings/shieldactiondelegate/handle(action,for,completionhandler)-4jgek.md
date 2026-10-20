# handle(action:for:completionHandler:)

**Framework**: Managed Settings  
**Kind**: method  
**Role**: Instance Method

Allows the extension to respond to a user action when the system displays a shield over an application.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func handle(action: ShieldAction, for application: ApplicationToken, completionHandler: @escaping (ShieldActionResponse) -> Void)
```

## Parameters

- `action`: The user’s action.
- `application`: The application that the shield covers.
- `completionHandler`: A closure for your extension to call after you handle the user’s action.

## See Also

### Responding to someone’s action
- [func handle(action: ShieldAction, for: ActivityCategoryToken, completionHandler: (ShieldActionResponse) -> Void)](./handle%28action,for,completionhandler%29-9hcqc.md)
  Allows the extension to respond to a user action when the system displays a shield over an application or website because of its category.
- [func handle(action: ShieldAction, for: WebDomainToken, completionHandler: (ShieldActionResponse) -> Void)](./handle%28action,for,completionhandler%29-4tqna.md)
  Allows the extension to respond to a user action when the system displays a shield over a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate/handle(action:for:completionhandler:)-4jgek)*