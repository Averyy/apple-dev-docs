# CPActionSheetTemplate

**Framework**: CarPlay  
**Kind**: class

A template that displays a modal action sheet.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPActionSheetTemplate
```

#### Overview

You must present action sheets modally by calling the [`presentTemplate(_:animated:completion:)`](cpinterfacecontroller/presenttemplate(_:animated:completion:).md) method available on your app’s instance of [`CPInterfaceController`](cpinterfacecontroller.md). The user dismisses the action sheet by pressing a button, or you can dismiss it by calling the interface controller’s [`dismissTemplate(animated:completion:)`](cpinterfacecontroller/dismisstemplate(animated:completion:).md) method.

## Topics

### Creating an Action Sheet Template
- [init(title: String?, message: String?, actions: [CPAlertAction])](cpactionsheettemplate/init(title:message:actions:).md)
  Creates an action sheet template.
### Getting Action Sheet Template Information
- [var title: String?](cpactionsheettemplate/title.md)
  The title of the action sheet.
- [var message: String?](cpactionsheettemplate/message.md)
  The descriptive message providing details about the reason for displaying the action sheet.
- [var actions: [CPAlertAction]](cpactionsheettemplate/actions.md)
  The list of actions available on the action sheet.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CPAlertTemplate](cpalerttemplate.md)
  A template that displays a modal alert.
- [class CPAlertAction](cpalertaction.md)
  An object that encapsulates an action the user can perform on an action sheet or alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpactionsheettemplate)*