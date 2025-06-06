# NSTextFieldDelegate

**Framework**: AppKit  
**Kind**: protocol

A protocol that a text field delegate can use to control its field editor action menu.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextFieldDelegate : NSControlTextEditingDelegate
```

## Topics

### Controlling Editing Behavior
- [func textField(NSTextField, textView: NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](nstextfielddelegate/textfield(_:textview:candidates:forselectedrange:).md)
- [func textField(NSTextField, textView: NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](nstextfielddelegate/textfield(_:textview:candidatesforselectedrange:).md)
- [func textField(NSTextField, textView: NSTextView, shouldSelectCandidateAt: Int) -> Bool](nstextfielddelegate/textfield(_:textview:shouldselectcandidateat:).md)

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSComboBoxDelegate](nscomboboxdelegate.md)
- [NSSearchFieldDelegate](nssearchfielddelegate.md)
- [NSTokenFieldDelegate](nstokenfielddelegate.md)

## See Also

- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
- [protocol NSTextDelegate](nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.
- [class NSText](nstext.md)
  The most general programmatic interface for objects that manage text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfielddelegate)*