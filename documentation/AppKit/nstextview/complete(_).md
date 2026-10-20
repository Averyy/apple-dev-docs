# complete(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invokes completion in a text view.

**Availability**:
- macOS

## Declaration

```swift
func complete(_ sender: Any?)
```

```objc
- (void) complete:(id) sender;
```

#### Discussion

By default invoked using the F5 key, this method provides users with a choice of completions for the word currently being typed. May be invoked programmatically if autocompletion is desired by a client of the text system. You can change the key invoking this method using the text system’s key bindings mechanism; see “[Text System Defaults and Key Bindings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TextDefaultsBindings/TextDefaultsBindings.html#//apple_ref/doc/uid/20000468)” for an explanation of the procedure.

The delegate may replace or modify the list of possible completions by implementing [`textView(_:completions:forPartialWordRange:indexOfSelectedItem:)`](../nstextviewdelegate/textview%28_,completions,forpartialwordrange,indexofselecteditem%29.md). Subclasses can control the list by overriding [`completions(forPartialWordRange:indexOfSelectedItem:)`](./completions%28forpartialwordrange,indexofselecteditem%29.md).

## Parameters

- `sender`: The control sending the message. May be `nil`.

## See Also

### Performing text completion
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](./completions%28forpartialwordrange,indexofselecteditem%29.md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](./insertcompletion%28_,forpartialwordrange,movement,isfinal%29.md)
  Inserts the selected completion into the text at the appropriate location.
- [var rangeForUserCompletion: NSRange](./rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/complete(_:))*