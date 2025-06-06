# buttons

**Framework**: AppKit  
**Kind**: property

The array of response buttons for the alert.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var buttons: [NSButton] { get }
```

#### Discussion

The button displayed rightmost in the alert (for a left-to-right language) corresponds to the button at index `0` in this property’s array, and is considered the default button. A user can invoke this button by pressing the Return key.

Any button with a title of “Cancel” has a key equivalent of Escape, and any button with the title “Don’t Save” has a key equivalent of Command-D (but only if it is not the first button). You can also assign different key equivalents for the buttons using the [`keyEquivalent`](nsbutton/keyequivalent.md) method of the `NSButton` class.

## See Also

- [func addButton(withTitle: String) -> NSButton](nsalert/addbutton(withtitle:).md)
  Adds a button with a given title to the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/buttons)*