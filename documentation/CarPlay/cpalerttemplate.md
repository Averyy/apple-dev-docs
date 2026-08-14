# CPAlertTemplate

**Framework**: CarPlay  
**Kind**: class

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

#### Overview

You must present alerts modally by calling the [`presentTemplate(_:animated:completion:)`](cpinterfacecontroller/presenttemplate(_:animated:completion:).md) method available on your app’s instance of [`CPInterfaceController`](cpinterfacecontroller.md). The user dismisses the alert by pressing a button, or you can dismiss it by calling the interface controller’s [`dismissTemplate(animated:completion:)`](cpinterfacecontroller/dismisstemplate(animated:completion:).md) method.

## Topics

### Creating an Alert Template
- [init(titleVariants: [String], actions: [CPAlertAction])](cpalerttemplate/init(titlevariants:actions:).md)
  Creates an alert template.
- [class var maximumActionCount: Int](cpalerttemplate/maximumactioncount.md)
  The maximum number of actions allowed in an alert template.
### Getting the Alert Information
- [var titleVariants: [String]](cpalerttemplate/titlevariants.md)
  The array of title variants.
- [var actions: [CPAlertAction]](cpalerttemplate/actions.md)
  The array of actions available on the alert.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CPActionSheetTemplate](cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertAction](cpalertaction.md)
  An object that encapsulates an action the user can perform on an action sheet or alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalerttemplate)*