# type

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A required, app-specific string that you can employ to identify the type of quick action to perform.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var type: String { get set }
```

```objc
@property (nonatomic, copy) NSString * type;
```

## See Also

### Inspecting a Home Screen dynamic mutable quick action
- [var localizedTitle: String](./localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic mutable quick action.
- [var localizedSubtitle: String?](./localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [var icon: UIApplicationShortcutIcon?](./icon.md)
  The optional icon for the Home Screen dynamic mutable quick action.
- [var userInfo: [String : any NSSecureCoding]?](./userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/type)*