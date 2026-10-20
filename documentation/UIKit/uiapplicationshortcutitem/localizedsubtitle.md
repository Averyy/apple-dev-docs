# localizedSubtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The optional, user-visible subtitle for the Home Screen dynamic quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedSubtitle: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * localizedSubtitle;
```

#### Discussion

If you specify a subtitle for a quick action, the system then displays the title on a single line (potentially with an ellipsis character), no matter how long the title is.

To internationalize the subtitle for a Home Screen dynamic quick action, employ the [`NSLocalizedString`](../../Foundation/nslocalizedstring.md) Foundation function, described in [Foundation Functions](../../Foundation/foundation-functions.md), along with a `Localized.strings` file in your Xcode project.

## See Also

### Inspecting a Home Screen dynamic quick action
- [var localizedTitle: String](./localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic quick action.
- [var type: String](./type.md)
  A required, app-specific string that you employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](./icon.md)
  The optional icon for the Home Screen dynamic quick action.
- [var userInfo: [String : any NSSecureCoding]?](./userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home screen quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/localizedsubtitle)*