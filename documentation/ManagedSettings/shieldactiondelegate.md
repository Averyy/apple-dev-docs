# ShieldActionDelegate

**Framework**: Managed Settings  
**Kind**: class  
**Role**: Class

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

## Overview

Subclass `ShieldActionDelegate` to allow client extensions to respond to user actions on a shield that covers an application or website. The system doesn’t provide the name of a shielded [`Application`](./application.md), [`WebDomain`](./webdomain.md), or [`ActivityCategory`](./activitycategory.md) to preserve the Family Sharing group’s privacy. Instead, the system uses a token to indicate what content it is shielding.

## Topics

### Handling shield actions
- [enum ShieldAction](./shieldaction.md)
  Constants that describe a user’s action for your extension to handle.
- [enum ShieldActionResponse](./shieldactionresponse.md)
  Constants your extension that handles shield actions can use to tell the system how to respond to an action.
### Responding to someone’s action
- [func handle(action: ShieldAction, for: ApplicationToken, completionHandler: (ShieldActionResponse) -> Void)](./shieldactiondelegate/handle%28action,for,completionhandler%29-4jgek.md)
  Allows the extension to respond to a user action when the system displays a shield over an application.
- [func handle(action: ShieldAction, for: ActivityCategoryToken, completionHandler: (ShieldActionResponse) -> Void)](./shieldactiondelegate/handle%28action,for,completionhandler%29-9hcqc.md)
  Allows the extension to respond to a user action when the system displays a shield over an application or website because of its category.
- [func handle(action: ShieldAction, for: WebDomainToken, completionHandler: (ShieldActionResponse) -> Void)](./shieldactiondelegate/handle%28action,for,completionhandler%29-4tqna.md)
  Allows the extension to respond to a user action when the system displays a shield over a website.
### Initializers
- [init()](./shieldactiondelegate/init%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shield actions
- [enum ShieldAction](./shieldaction.md)
  Constants that describe a user’s action for your extension to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate)*