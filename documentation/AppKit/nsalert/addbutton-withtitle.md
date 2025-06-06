# addButton(withTitle:)

**Framework**: AppKit  
**Kind**: method

Adds a button with a given title to the alert.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addButton(withTitle title: String) -> NSButton
```

#### Return Value

Button added to the alert.

#### Discussion

Buttons are placed starting near the right side of the alert and going toward the left side (for languages that read left to right). The first three buttons are identified positionally as `NSAlertFirstButtonReturn`, `NSAlertSecondButtonReturn`, `NSAlertThirdButtonReturn` in the return-code parameter evaluated by the modal delegate. Subsequent buttons are identified as `NSAlertThirdButtonReturn` +`n`, where `n` is an integer

By default, the first button has a key equivalent of Return, any button with a title of “Cancel” has a key equivalent of Escape, and any button with the title “Don’t Save” has a key equivalent of Command-D (but only if it’s  the first button). You can also assign different key equivalents for the buttons using the [`keyEquivalent`](nsbutton/keyequivalent.md) method of the `NSButton` class. In addition, you can use the [`tag`](nscontrol/tag.md) method of the `NSButton` class to set the return value.

## Parameters

- `title`: Title of the button to add to the alert. Must not be  .

## See Also

- [class NSAlert](nsalert.md)
  A modal dialog or sheet attached to a document window.
- [var buttons: [NSButton]](nsalert/buttons.md)
  The array of response buttons for the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/addbutton(withtitle:))*