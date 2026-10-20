# rangeForUserCompletion

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The partial range from the most recent beginning of a word up to the insertion point.

**Availability**:
- macOS

## Declaration

```swift
var rangeForUserCompletion: NSRange { get }
```

```objc
@property (readonly) NSRange rangeForUserCompletion;
```

#### Discussion

This value is intended to be used for the range argument in the text completion methods such as [`completions(forPartialWordRange:indexOfSelectedItem:)`](./completions%28forpartialwordrange,indexofselecteditem%29.md).

## See Also

### Performing text completion
- [func complete(Any?)](./complete%28_%29.md)
  Invokes completion in a text view.
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](./completions%28forpartialwordrange,indexofselecteditem%29.md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](./insertcompletion%28_,forpartialwordrange,movement,isfinal%29.md)
  Inserts the selected completion into the text at the appropriate location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rangeforusercompletion)*