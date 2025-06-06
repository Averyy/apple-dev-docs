# icon

**Framework**: UIKit  
**Kind**: property

The optional icon for the Home Screen dynamic quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var icon: UIApplicationShortcutIcon? { get }
```

#### Discussion

Quick action icons are template (alpha-channel-only) images that you typically provide as part of an asset catalog. For more information, see [`UIApplicationShortcutIcon`](uiapplicationshortcuticon.md).

## See Also

- [var localizedTitle: String](uiapplicationshortcutitem/localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic quick action.
- [var localizedSubtitle: String?](uiapplicationshortcutitem/localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic quick action.
- [var type: String](uiapplicationshortcutitem/type.md)
  A required, app-specific string that you employ to identify the type of quick action to perform.
- [var userInfo: [String : any NSSecureCoding]?](uiapplicationshortcutitem/userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home screen quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/icon)*