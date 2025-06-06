# delete(in:to:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Deletes text by the specified direction and granularity.  Current supported combinations include:

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func delete(in direction: UITextStorageDirection, to granularity: UITextGranularity)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Character backward  = delete character forward = delete-forward word backward = option + delete word forward = option + delete-forward line end = cmd + delete line start = cmd + delete-forward paragraph  end = ctrl + K paragraph start = ctrl + fn + K

(On Apple keyboards, the delete-forward key is a combination of fn + delete)

Deletes the specified amount of text.

## Parameters

- `direction`: The direction in which to delete text, relative to the base writing direction.
- `granularity`: The amount of text to delete.

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
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](betextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/delete(in:to:))*