# NSTextContent

**Framework**: AppKit  
**Kind**: protocol

A protocol that describes specific kinds of input content types.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextContent
```

## Topics

### Specifying content type
- [var contentType: NSTextContentType?](nstextcontent/contenttype.md)
  The semantic meaning for a text input area.
- [struct NSTextContentType](nstextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.

## Relationships

### Conforming Types
- [NSComboBox](nscombobox.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSTextField](nstextfield.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)

## See Also

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontent)*