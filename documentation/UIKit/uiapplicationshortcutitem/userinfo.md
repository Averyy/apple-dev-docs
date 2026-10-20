# userInfo

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Optional, app-specific information that you can provide for use when your app performs the Home screen quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [String : any NSSecureCoding]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDictionary<NSString *,id<NSSecureCoding>> * userInfo;
```

#### Discussion

The keys and values in this property’s dictionary must conform to the [`NSSecureCoding`](../../Foundation/nssecurecoding.md) protocol, and must be property-list-encodable. If they aren’t, the system raises a runtime exception when initializing the quick action. For information about property-list-encodable data, see [Serializing Property Lists](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html#//apple_ref/doc/uid/20000952) in [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i) and see [`PropertyListSerialization`](../../Foundation/propertylistserialization.md).

## See Also

### Inspecting a Home Screen dynamic quick action
- [var localizedTitle: String](./localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic quick action.
- [var localizedSubtitle: String?](./localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic quick action.
- [var type: String](./type.md)
  A required, app-specific string that you employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](./icon.md)
  The optional icon for the Home Screen dynamic quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/userinfo)*