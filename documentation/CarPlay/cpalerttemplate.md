# CPAlertTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a modal alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPAlertTemplate
```

```objc
@interface CPAlertTemplate : CPTemplate
```

## Overview

You must present alerts modally by calling the [`presentTemplate(_:animated:completion:)`](./cpinterfacecontroller/presenttemplate%28_,animated,completion%29.md) method available on your app’s instance of [`CPInterfaceController`](./cpinterfacecontroller.md). The user dismisses the alert by pressing a button, or you can dismiss it by calling the interface controller’s [`dismissTemplate(animated:completion:)`](./cpinterfacecontroller/dismisstemplate%28animated,completion%29.md) method.

## Topics

### Creating an Alert Template
- [init(titleVariants: [String], actions: [CPAlertAction])](./cpalerttemplate/init%28titlevariants,actions%29.md)
  Creates an alert template.
- [class var maximumActionCount: Int](./cpalerttemplate/maximumactioncount.md)
  The maximum number of actions allowed in an alert template.
### Getting the Alert Information
- [var titleVariants: [String]](./cpalerttemplate/titlevariants.md)
  The array of title variants.
- [var actions: [CPAlertAction]](./cpalerttemplate/actions.md)
  The array of actions available on the alert.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Actions and Alerts
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertAction](./cpalertaction.md)
  An object that encapsulates an action the user can perform on an action sheet or alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalerttemplate)*