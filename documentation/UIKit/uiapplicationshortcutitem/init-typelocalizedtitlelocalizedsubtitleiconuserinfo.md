# init(type:localizedTitle:localizedSubtitle:icon:userInfo:)

**Framework**: UIKit  
**Kind**: init

Creates an immutable Home Screen dynamic quick action with user-visible title, icon, and user info dictionary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(type: String, localizedTitle: String, localizedSubtitle: String?, icon: UIApplicationShortcutIcon?, userInfo: [String : any NSSecureCoding]? = nil)
```

#### Return Value

An immutable Home Screen dynamic quick action item with a user-visible title, optional subtitle, optional icon, and optional user info dictionary.

## Parameters

- `type`: The required, app-defined type of the Home Screen quick action.
- `localizedTitle`: The required, user-visible title of the Home Screen quick action.
- `localizedSubtitle`: The optional, user-visible subtitle of the Home Screen quick action.
- `icon`: The optional icon for the Home Screen quick action.
- `userInfo`: One common, important use for this dictionary is to specify the version of your app. If a user installs an update for your app but hasn’t yet launched the update, pressing your Home Screen icon shows the dynamic quick actions for the previously-installed version. Including the app version in the   dictionary lets you gracefully handle this scenario.

## See Also

- [convenience init(type: String, localizedTitle: String)](uiapplicationshortcutitem/init(type:localizedtitle:).md)
  Creates an immutable Home Screen dynamic quick action with a user-visible title and no icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/init(type:localizedtitle:localizedsubtitle:icon:userinfo:))*