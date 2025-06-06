# rangeForUserCompletion

**Framework**: AppKit  
**Kind**: property

The partial range from the most recent beginning of a word up to the insertion point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rangeForUserCompletion: NSRange { get }
```

#### Discussion

This value is intended to be used for the range argument in the text completion methods such as [`completions(forPartialWordRange:indexOfSelectedItem:)`](nstextview/completions(forpartialwordrange:indexofselecteditem:).md).

## See Also

- [func complete(Any?)](nstextview/complete(_:).md)
  Invokes completion in a text view.
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](nstextview/completions(forpartialwordrange:indexofselecteditem:).md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](nstextview/insertcompletion(_:forpartialwordrange:movement:isfinal:).md)
  Inserts the selected completion into the text at the appropriate location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/rangeforusercompletion)*