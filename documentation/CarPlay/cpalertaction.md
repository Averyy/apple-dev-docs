# CPAlertAction

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that encapsulates an action the user can perform on an action sheet or alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPAlertAction
```

```objc
@interface CPAlertAction : NSObject
```

## Overview

Use an alert action to display a button on an alert. The combination of the alert and the action styles determines the appearance of the action button. To perform an action after the user taps the button, provide a block to the action’s [`handler`](./cpalertaction/handler.md) property.

## Topics

### Creating an Alert Action
- [init(title: String, style: CPAlertAction.Style, handler: CPAlertActionHandler)](./cpalertaction/init%28title,style,handler%29.md)
  Creates an alert action with a title, style, and action handler.
### Getting the Title
- [var title: String](./cpalertaction/title.md)
  The action button’s title.
### Getting the Action Style
- [var style: CPAlertAction.Style](./cpalertaction/style-swift.property.md)
  The display style for the action button.
- [CPAlertAction.Style](./cpalertaction/style-swift.enum.md)
  Display styles for an alert’s action button.
### Getting the Action Handler
- [var handler: CPAlertActionHandler](./cpalertaction/handler.md)
  The closure that CarPlay invokes after the user taps the action button.
- [typealias CPAlertActionHandler](./cpalertactionhandler.md)
  The declaration for an alert action handler.
### Initializers
- [init(title: String, color: UIColor, handler: CPAlertActionHandler)](./cpalertaction/init%28title,color,handler%29.md)
- [init?(coder: NSCoder)](./cpalertaction/init%28coder%29.md)
### Instance Properties
- [var color: UIColor?](./cpalertaction/color.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Actions and Alerts
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertaction)*