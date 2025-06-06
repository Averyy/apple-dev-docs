# userInfo

**Framework**: UIKit  
**Kind**: property

Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [String : any NSSecureCoding]? { get set }
```

#### Discussion

The keys and values in this property’s dictionary must conform to the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol, and must be property-list-encodable. If they aren’t, the system raises a runtime exception when initializing the quick action. For information about property-list-encodable data, see [`Serializing Property Lists`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html#//apple_ref/doc/uid/20000952) in [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) and see [`PropertyListSerialization`](https://developer.apple.com/documentation/Foundation/PropertyListSerialization).

## See Also

- [var localizedTitle: String](uimutableapplicationshortcutitem/localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic mutable quick action.
- [var localizedSubtitle: String?](uimutableapplicationshortcutitem/localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [var type: String](uimutableapplicationshortcutitem/type.md)
  A required, app-specific string that you can employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](uimutableapplicationshortcutitem/icon.md)
  The optional icon for the Home Screen dynamic mutable quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/userinfo)*