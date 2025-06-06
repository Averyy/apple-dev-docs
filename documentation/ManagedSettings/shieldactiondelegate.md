# ShieldActionDelegate

**Framework**: ManagedSettings  
**Kind**: class

A class for an extension that handles shield actions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@objc
class ShieldActionDelegate
```

#### Overview

Subclass `ShieldActionDelegate` to allow client extensions to respond to user actions on a shield that covers an application or website. The system doesn’t provide the name of a shielded [`Application`](application.md), [`WebDomain`](webdomain.md), or [`ActivityCategory`](activitycategory.md) to preserve the Family Sharing group’s privacy. Instead, the system uses a token to indicate what content it is shielding.

## Topics

### Handling Shield Actions
- [enum ShieldAction](shieldaction.md)
  Constants that describe a user’s action for your extension to handle.
- [enum ShieldActionResponse](shieldactionresponse.md)
  Constants your extension that handles shield actions can use to tell the system how to respond to an action.
### Initializers
- [init()](shieldactiondelegate/init.md)
### Instance Methods
- [func handle(action: ShieldAction, for: ApplicationToken, completionHandler: (ShieldActionResponse) -> Void)](shieldactiondelegate/handle(action:for:completionhandler:)-4jgek.md)
  Allows the extension to respond to a user action when the system displays a shield over an application.
- [func handle(action: ShieldAction, for: WebDomainToken, completionHandler: (ShieldActionResponse) -> Void)](shieldactiondelegate/handle(action:for:completionhandler:)-4tqna.md)
  Allows the extension to respond to a user action when the system displays a shield over a website.
- [func handle(action: ShieldAction, for: ActivityCategoryToken, completionHandler: (ShieldActionResponse) -> Void)](shieldactiondelegate/handle(action:for:completionhandler:)-9hcqc.md)
  Allows the extension to respond to a user action when the system displays a shield over an application or website because of its category.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate)*