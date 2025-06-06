# UIMutableApplicationShortcutItem

**Framework**: UIKit  
**Kind**: class

A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIMutableApplicationShortcutItem
```

#### Overview

This class is a convenience subclass of [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md), helping you work with registered, and therefore immutable, quick actions. For information about how to use objects of this class in your app, read the overview in [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md).

## Topics

### Inspecting a Home Screen dynamic mutable quick action
- [var localizedTitle: String](uimutableapplicationshortcutitem/localizedtitle.md)
  The required, user-visible title for the Home Screen dynamic mutable quick action.
- [var localizedSubtitle: String?](uimutableapplicationshortcutitem/localizedsubtitle.md)
  The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [var type: String](uimutableapplicationshortcutitem/type.md)
  A required, app-specific string that you can employ to identify the type of quick action to perform.
- [var icon: UIApplicationShortcutIcon?](uimutableapplicationshortcutitem/icon.md)
  The optional icon for the Home Screen dynamic mutable quick action.
- [var userInfo: [String : any NSSecureCoding]?](uimutableapplicationshortcutitem/userinfo.md)
  Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.
### Designating the scene to activate
- [var targetContentIdentifier: Any?](uimutableapplicationshortcutitem/targetcontentidentifier.md)
  The object that determines which scene handles the quick action.

## Relationships

### Inherits From
- [UIApplicationShortcutItem](uiapplicationshortcutitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Add Home Screen quick actions](add-home-screen-quick-actions.md)
  Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.
- [class UIApplicationShortcutItem](uiapplicationshortcutitem.md)
  An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.
- [class UIApplicationShortcutIcon](uiapplicationshortcuticon.md)
  An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem)*