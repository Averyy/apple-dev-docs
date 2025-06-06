# complete(_:)

**Framework**: AppKit  
**Kind**: method

Invokes completion in a text view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func complete(_ sender: Any?)
```

#### Discussion

By default invoked using the F5 key, this method provides users with a choice of completions for the word currently being typed. May be invoked programmatically if autocompletion is desired by a client of the text system. You can change the key invoking this method using the text system’s key bindings mechanism; see “[`Text System Defaults and Key Bindings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TextDefaultsBindings/TextDefaultsBindings.html#//apple_ref/doc/uid/20000468)” for an explanation of the procedure.

The delegate may replace or modify the list of possible completions by implementing [`textView(_:completions:forPartialWordRange:indexOfSelectedItem:)`](nstextviewdelegate/textview(_:completions:forpartialwordrange:indexofselecteditem:).md). Subclasses can control the list by overriding [`completions(forPartialWordRange:indexOfSelectedItem:)`](nstextview/completions(forpartialwordrange:indexofselecteditem:).md).

## Parameters

- `sender`: The control sending the message. May be  .

## See Also

- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](nstextview/completions(forpartialwordrange:indexofselecteditem:).md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](nstextview/insertcompletion(_:forpartialwordrange:movement:isfinal:).md)
  Inserts the selected completion into the text at the appropriate location.
- [var rangeForUserCompletion: NSRange](nstextview/rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/complete(_:))*