# init(identifier:title:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a user notification action with a specified identifier and title.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
convenience init(identifier: String?, title: String?)
```

```objc
+ (instancetype) actionWithIdentifier:(NSString *) identifier title:(NSString *) title;
```

## Parameters

- `identifier`: The identifier for the action.
- `title`: A localized string suitable for display to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationaction/init(identifier:title:))*