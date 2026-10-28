# localizedTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The required, user-visible title for the Home Screen dynamic mutable quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedTitle: String { get set }
```

```objc
@property (nonatomic, copy) NSString * localizedTitle;
```

## Discussion

Every Home Screen mutable quick action must have a user-visible title.

If the title fits on one line, the system displays it as a single line quick action. If the title is too long for one line and you have not specified a [`localizedSubtitle`](./localizedsubtitle.md) string, the system displays the title on two lines.

To internationalize the title for a Home Screen dynamic quick action, employ the [`NSLocalizedString`](../../Foundation/nslocalizedstring.md) Foundation function, described in [Foundation Functions](../../Foundation/foundation-functions.md), along with a `Localizable.strings` file in your Xcode project.

## See Also

### Inspecting a Home Screen dynamic mutable quick action
- [var localizedSubtitle: String?](./localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [var type: String](./type.md)
  A required, app-specific string that you can employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](./icon.md)
  The optional icon for the Home Screen dynamic mutable quick action.
- [var userInfo: [String : any NSSecureCoding]?](./userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/localizedtitle)*