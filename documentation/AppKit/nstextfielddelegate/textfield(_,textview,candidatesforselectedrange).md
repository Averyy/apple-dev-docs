# textField(_:textView:candidatesForSelectedRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides a customized list of candidates to the text view’s `candidateListTouchBarItem`. This method returns an array of objects that represent the elements of a selection.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func textField(_ textField: NSTextField, textView: NSTextView, candidatesForSelectedRange selectedRange: NSRange) -> [Any]?
```

```objc
- (NSArray *) textField:(NSTextField *) textField textView:(NSTextView *) textView candidatesForSelectedRange:(NSRange) selectedRange;
```

## Discussion

Invoked from `updateCandidates`. `NSTextView` uses the candidates returned from this method and suppress its built-in candidate generation. Returning `nil` from this delegate method allows `NSTextView` to query candidates from `NSSpellChecker`.

## See Also

### Controlling Editing Behavior
- [func textField(NSTextField, textView: NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./textfield%28_,textview,candidates,forselectedrange%29.md)
  Allows customizing the candidate list queried from `NSSpellChecker`. This method returns array of text objects to include in a text selection.
- [func textField(NSTextField, textView: NSTextView, shouldSelectCandidateAt: Int) -> Bool](./textfield%28_,textview,shouldselectcandidateat%29.md)
  Notifies the delegate that the user selected the candidate at index in `-[NSCandidateListTouchBarItem candidates]` for the text view’s `candidateListTouchBarItem`. Returns a Boolean value that indicates whether to select the text object at the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfielddelegate/textfield(_:textview:candidatesforselectedrange:))*