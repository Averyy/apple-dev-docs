# localizedSubtitle

**Framework**: UIKit  
**Kind**: property

The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedSubtitle: String? { get set }
```

#### Discussion

If you specify a subtitle for a mutable quick action, the system then displays the title on a single line (potentially with an ellipsis character), no matter how long the title is.

To internationalize the subtitle for a Home Screen mutable, dynamic quick action, employ the [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) Foundation function, described in [`Foundation Functions`](https://developer.apple.com/documentation/Foundation/foundation-functions), along with a `Localized.strings` file in your Xcode project.

## See Also

- [var localizedTitle: String](uimutableapplicationshortcutitem/localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic mutable quick action.
- [var type: String](uimutableapplicationshortcutitem/type.md)
  A required, app-specific string that you can employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](uimutableapplicationshortcutitem/icon.md)
  The optional icon for the Home Screen dynamic mutable quick action.
- [var userInfo: [String : any NSSecureCoding]?](uimutableapplicationshortcutitem/userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/localizedsubtitle)*