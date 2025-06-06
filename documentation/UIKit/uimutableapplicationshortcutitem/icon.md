# icon

**Framework**: UIKit  
**Kind**: property

The optional icon for the Home Screen dynamic mutable quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var icon: UIApplicationShortcutIcon? { get set }
```

#### Discussion

Quick action icons are template (alpha-channel-only) images that you typically provide as part of an asset catalog. For more information, see [`UIApplicationShortcutIcon`](uiapplicationshortcuticon.md).

## See Also

- [var localizedTitle: String](uimutableapplicationshortcutitem/localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic mutable quick action.
- [var localizedSubtitle: String?](uimutableapplicationshortcutitem/localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [var type: String](uimutableapplicationshortcutitem/type.md)
  A required, app-specific string that you can employ to identify the type of quick action to perform.
- [var userInfo: [String : any NSSecureCoding]?](uimutableapplicationshortcutitem/userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/icon)*