# NSTextInputClient

**Framework**: AppKit  
**Kind**: protocol

A set of methods that text views need to implement to interact properly with the text input management system.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextInputClient
```

## Mentions

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)

#### Overview

To create another text view class, you can either subclass [`NSTextView`](nstextview.md), or subclass [`NSView`](nsview.md) and implement the [`NSTextInputClient`](nstextinputclient.md) protocol.

> ❗ **Important**:  Methods specific to the [`NSTextInputClient`](nstextinputclient.md) protocol are intended for dealing with text input and generally aren’t suitable for other purposes.

## Topics

### Handling marked text
- [func hasMarkedText() -> Bool](nstextinputclient/hasmarkedtext.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](nstextinputclient/markedrange.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:).md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func unmarkText()](nstextinputclient/unmarktext.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](nstextinputclient/validattributesformarkedtext.md)
  Returns an array of attribute names recognized by the receiver.
### Storing text
- [func attributedString() -> NSAttributedString](nstextinputclient/attributedstring.md)
  Returns an attributed string representing the receiver’s text storage.
- [func attributedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](nstextinputclient/attributedsubstring(forproposedrange:actualrange:).md)
  Returns an attributed string derived from the given range in the receiver’s text storage.
- [func insertText(Any, replacementRange: NSRange)](nstextinputclient/inserttext(_:replacementrange:).md)
  Inserts the given string into the receiver, replacing the specified content.
### Getting character coordinates
- [func characterIndex(for: NSPoint) -> Int](nstextinputclient/characterindex(for:).md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](nstextinputclient/firstrect(forcharacterrange:actualrange:).md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](nstextinputclient/baselinedeltaforcharacter(at:).md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).
- [func drawsVerticallyForCharacter(at: Int) -> Bool](nstextinputclient/drawsverticallyforcharacter(at:).md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](nstextinputclient/fractionofdistancethroughglyph(for:).md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.
### Placing content
- [var documentVisibleRect: NSRect](nstextinputclient/documentvisiblerect.md)
- [var unionRectInVisibleSelectedRange: NSRect](nstextinputclient/unionrectinvisibleselectedrange.md)
- [func preferredTextAccessoryPlacement() -> NSTextCursorAccessoryPlacement](nstextinputclient/preferredtextaccessoryplacement.md)
- [func windowLevel() -> Int](nstextinputclient/windowlevel.md)
  Returns the window level of the receiver.
### Binding keystrokes
- [func doCommand(by: Selector)](nstextinputclient/docommand(by:).md)
  Invokes the action specified by the given selector.
### Supporting adaptive images
- [var supportsAdaptiveImageGlyph: Bool](nstextinputclient/supportsadaptiveimageglyph.md)
  A Boolean value that indicates whether the document supports adaptive images in the input.
- [func insert(NSAdaptiveImageGlyph, replacementRange: NSRange)](nstextinputclient/insert(_:replacementrange:).md)
  Inserts an adaptive image into the text at the specifed location.

## Relationships

### Inherited By
- [NSTextCheckingClient](nstextcheckingclient.md)
### Conforming Types
- [NSTextView](nstextview.md)

## See Also

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient)*