# textField(_:textView:shouldSelectCandidateAt:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that the user selected the candidate at index in `-[NSCandidateListTouchBarItem candidates]` for the text view’s `candidateListTouchBarItem`. Returns a Boolean value that indicates whether to select the text object at the index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func textField(_ textField: NSTextField, textView: NSTextView, shouldSelectCandidateAt index: Int) -> Bool
```

## Parameters

- `textField`: The text field that sent the message.
- `textView`: The text view that sent the message.
- `index`: The index that represents the start of the candidate text to evaluate, or `NSNotFound` if no candidate is to be selected.

## See Also

- [func textField(NSTextField, textView: NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](nstextfielddelegate/textfield(_:textview:candidates:forselectedrange:).md)
  Allows customizing the candidate list queried from `NSSpellChecker`. This method returns array of text objects to include in a text selection.
- [func textField(NSTextField, textView: NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](nstextfielddelegate/textfield(_:textview:candidatesforselectedrange:).md)
  Provides a customized list of candidates to the text view’s `candidateListTouchBarItem`. This method returns an array of objects that represent the elements of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfielddelegate/textfield(_:textview:shouldselectcandidateat:))*