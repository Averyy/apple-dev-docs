# NSTokenField

**Framework**: AppKit  
**Kind**: class

A text field that converts text into visually distinct tokens.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTokenField
```

#### Overview

Use a token field when you want typed text to be transformed into “tokens”, which are visually distinct elements in the text field interface. For example, you might use a token field in a mail app to display email addresses for individual users. The distinct appearance of tokens makes them easy for users to distinguish from surrounding text.

`NSTokenField` uses an [`NSTokenFieldCell`](nstokenfieldcell.md) to implement much of the control’s functionality. `NSTokenField` provides cover methods for most methods of `NSTokenFieldCell`, which invoke the corresponding cell method.

> **Note**:  In OS X v10.4 and earlier, represented objects associated with token fields had to conform to [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding). Starting with OS X v10.5, they no longer need to. In OS X v10.4, `NSTokenField` trims whitespace around tokens but it does not trim whitespace in macOS versions 10.5.0 and 10.5.1. In OS X v10.5.2, you get whitespace-trimming behavior by either linking against the v10.4 binary or linking against the v10.5 binary and  implementing the [`tokenField(_:representedObjectForEditing:)`](nstokenfielddelegate/tokenfield(_:representedobjectforediting:).md) method. If you do not want the whitespace-trimming behavior, link against the v10.5 binary and implement this method, returning the editing string if you have no represented object.

## Topics

### Configuring the Token Style
- [var tokenStyle: NSTokenField.TokenStyle](nstokenfield/tokenstyle-swift.property.md)
  The token style of the receiver.
### Configuring the Tokenizing Character Set
- [var tokenizingCharacterSet: CharacterSet!](nstokenfield/tokenizingcharacterset.md)
  The recevier’s tokenizing character set to `characterSet`.
- [class var defaultTokenizingCharacterSet: CharacterSet](nstokenfield/defaulttokenizingcharacterset.md)
  Returns the default tokenizing character set.
### Configuring the Completion Delay
- [var completionDelay: TimeInterval](nstokenfield/completiondelay.md)
  The receiver’s completion delay.
- [class var defaultCompletionDelay: TimeInterval](nstokenfield/defaultcompletiondelay.md)
  Returns the default completion delay.
### Getting and Setting the Delegate
- [var delegate: (any NSTokenFieldDelegate)?](nstokenfield/delegate.md)
  Returns the token field’s delegate.
### Enumerations
- [NSTokenField.TokenStyle](nstokenfield/tokenstyle-swift.enum.md)
  The NSTokenStyle constants define how tokens are displayed and editable in the `NSTokenFieldCell`. These values are used by [`tokenStyle`](nstokenfieldcell/tokenstyle.md) and the delegate method [`tokenFieldCell(_:styleForRepresentedObject:)`](nstokenfieldcelldelegate/tokenfieldcell(_:styleforrepresentedobject:).md).

## Relationships

### Inherits From
- [NSTextField](nstextfield.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextContent](nstextcontent.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfield)*