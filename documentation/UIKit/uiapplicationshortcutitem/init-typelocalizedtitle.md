# init(type:localizedTitle:)

**Framework**: UIKit  
**Kind**: init

Creates an immutable Home Screen dynamic quick action with a user-visible title and no icon.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(type: String, localizedTitle: String)
```

#### Return Value

An immutable Home Screen dynamic quick action with a user-visible title and no icon.

## Parameters

- `type`: The required, app-defined type of the Home Screen quick action.
- `localizedTitle`: The required, user-visible title of the Home Screen quick action.

## See Also

- [init(type: String, localizedTitle: String, localizedSubtitle: String?, icon: UIApplicationShortcutIcon?, userInfo: [String : any NSSecureCoding]?)](uiapplicationshortcutitem/init(type:localizedtitle:localizedsubtitle:icon:userinfo:).md)
  Creates an immutable Home Screen dynamic quick action with user-visible title, icon, and user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:))*