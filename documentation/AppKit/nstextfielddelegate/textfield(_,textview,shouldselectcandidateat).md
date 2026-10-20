# textField(_:textView:shouldSelectCandidateAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the user selected the candidate at index in `-[NSCandidateListTouchBarItem candidates]` for the text view’s `candidateListTouchBarItem`. Returns a Boolean value that indicates whether to select the text object at the index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func textField(_ textField: NSTextField, textView: NSTextView, shouldSelectCandidateAt index: Int) -> Bool
```

```objc
- (BOOL) textField:(NSTextField *) textField textView:(NSTextView *) textView shouldSelectCandidateAtIndex:(NSUInteger) index;
```

## Parameters

- `textField`: The text field that sent the message.
- `textView`: The text view that sent the message.
- `index`: The index that represents the start of the candidate text to evaluate, or `NSNotFound` if no candidate is to be selected.

## See Also

### Controlling Editing Behavior
- [func textField(NSTextField, textView: NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./textfield%28_,textview,candidates,forselectedrange%29.md)
  Allows customizing the candidate list queried from `NSSpellChecker`. This method returns array of text objects to include in a text selection.
- [func textField(NSTextField, textView: NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](./textfield%28_,textview,candidatesforselectedrange%29.md)
  Provides a customized list of candidates to the text view’s `candidateListTouchBarItem`. This method returns an array of objects that represent the elements of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfielddelegate/textfield(_:textview:shouldselectcandidateat:))*