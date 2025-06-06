# setBaseWritingDirection(_:for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Sets the base writing direction for a specified range of text in a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, for range: UITextRange)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Informs the text view of the writing direction for a given range of text.

- writingDirection: Whether the writing direction is left-to-right, right-to-left, or the natural direction for the current script.
- range: The range in the text view’s document for which the writing direction applies.

## See Also

- [var isEditable: Bool](betextinput/iseditable.md)
  Reflects the ability to modify text
- [func handleKeyEntry(BEKeyEntry, completionHandler: (BEKeyEntry, Bool) -> Void)](betextinput/handlekeyentry(_:completionhandler:).md)
  Accepts key-entry events from the text system for the text view to process.
- [func shiftKeyStateChanged(fromState: BEKeyModifierFlags, toState: BEKeyModifierFlags)](betextinput/shiftkeystatechanged(fromstate:tostate:).md)
  Indicates a transition in shift state
- [func text(in: UITextRange) -> String?](betextinput/text(in:).md)
  Returns the text in the specified range.
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](betextinput/offset(from:to:).md)
  Returns the number of UTF-16 characters between one text position and another text position.
- [func delete(in: UITextStorageDirection, to: UITextGranularity)](betextinput/delete(in:to:).md)
  Deletes text by the specified direction and granularity.  Current supported combinations include:


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/setbasewritingdirection(_:for:))*