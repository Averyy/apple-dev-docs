# handle(action:for:completionHandler:)

**Framework**: ManagedSettings  
**Kind**: method

Allows the extension to respond to a user action when the system displays a shield over an application or website because of its category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func handle(action: ShieldAction, for category: ActivityCategoryToken, completionHandler: @escaping (ShieldActionResponse) -> Void)
```

## Parameters

- `action`: The user’s action.
- `category`: The category of the application or website that the shield covers.
- `completionHandler`: A closure for your extension to call after you handle the user’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate/handle(action:for:completionhandler:)-9hcqc)*