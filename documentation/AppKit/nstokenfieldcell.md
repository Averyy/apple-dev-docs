# NSTokenFieldCell

**Framework**: AppKit  
**Kind**: class

A text field cell subclass that enables tokenized editing of an array of objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTokenFieldCell
```

#### Overview

[`NSTokenFieldCell`](nstokenfieldcell.md) is a subclass of [`NSTextFieldCell`](nstextfieldcell.md) that provides tokenized editing of an array of objects similar to the address field in the Mail app. The objects may be strings or objects that can be represented as strings. A single token field cell can be presented in an [`NSTokenField`](nstokenfield.md) control.

## Topics

### Managing the Token Style
- [var tokenStyle: NSTokenField.TokenStyle](nstokenfieldcell/tokenstyle.md)
  The token style of the receiver.
### Managing the Tokenizing Character Set
- [class var defaultTokenizingCharacterSet: CharacterSet](nstokenfieldcell/defaulttokenizingcharacterset.md)
  Returns the default tokenizing character set.
- [var tokenizingCharacterSet: CharacterSet!](nstokenfieldcell/tokenizingcharacterset.md)
  The receiver’s tokenizing character set to a given character set.
### Configuring the Completion Delay
- [var completionDelay: TimeInterval](nstokenfieldcell/completiondelay.md)
  The receiver’s completion delay to a given delay.
- [class var defaultCompletionDelay: TimeInterval](nstokenfieldcell/defaultcompletiondelay.md)
  Returns the default completion delay.
### Managing the Delegate
- [var delegate: (any NSTokenFieldCellDelegate)?](nstokenfieldcell/delegate.md)
  The receiver’s delegate.
### Constants
- [NSTokenField.TokenStyle](nstokenfield/tokenstyle-swift.enum.md)
  The NSTokenStyle constants define how tokens are displayed and editable in the `NSTokenFieldCell`. These values are used by [`tokenStyle`](nstokenfieldcell/tokenstyle.md) and the delegate method [`tokenFieldCell(_:styleForRepresentedObject:)`](nstokenfieldcelldelegate/tokenfieldcell(_:styleforrepresentedobject:).md).

## Relationships

### Inherits From
- [NSTextFieldCell](nstextfieldcell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSTokenFieldCellDelegate](nstokenfieldcelldelegate.md)
  A set of optional methods implemented by delegates of [`NSTokenFieldCell`](nstokenfieldcell.md) objects to work with tokenized strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcell)*