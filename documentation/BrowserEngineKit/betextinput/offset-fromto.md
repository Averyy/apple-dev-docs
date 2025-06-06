# offset(from:to:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns the number of UTF-16 characters between one text position and another text position.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func offset(from: UITextPosition, to toPosition: UITextPosition) -> Int
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Returns the distance between two positions in the text view’s text.

## See Also

- [var isEditable: Bool](betextinput/iseditable.md)
  Reflects the ability to modify text
- [func handleKeyEntry(BEKeyEntry, completionHandler: (BEKeyEntry, Bool) -> Void)](betextinput/handlekeyentry(_:completionhandler:).md)
  Accepts key-entry events from the text system for the text view to process.
- [func shiftKeyStateChanged(fromState: BEKeyModifierFlags, toState: BEKeyModifierFlags)](betextinput/shiftkeystatechanged(fromstate:tostate:).md)
  Indicates a transition in shift state
- [func text(in: UITextRange) -> String?](betextinput/text(in:).md)
  Returns the text in the specified range.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](betextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.
- [func delete(in: UITextStorageDirection, to: UITextGranularity)](betextinput/delete(in:to:).md)
  Deletes text by the specified direction and granularity.  Current supported combinations include:


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/offset(from:to:))*