# allowsMixedState

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the button allows a mixed state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsMixedState: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the button has three states (on, off, and mixed), or [`false`](https://developer.apple.com/documentation/Swift/false) if the button has two states (on and off). The default value is [`false`](https://developer.apple.com/documentation/Swift/false). On and off states (also referred to as alternate and normal) indicate that the button is either clicked or not clicked. Mixed state is typically used for checkboxes or radio buttons. For example, suppose the state of a checkbox is used to denote whether a text field contains bold text. If all of the text in the text field is bold, then the checkbox appears checked (on). If none of the text is bold, then the checkbox appears unchecked (off). If some of the text is bold, then the checkbox contains a dash (mixed).

## See Also

- [var state: NSControl.StateValue](nsbutton/state.md)
  The button’s state.
- [func setNextState()](nsbutton/setnextstate.md)
  Sets the button to its next state.
- [func highlight(Bool)](nsbutton/highlight(_:).md)
  Highlights (or unhighlights) the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/allowsmixedstate)*