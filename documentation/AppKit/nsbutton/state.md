# state

**Framework**: AppKit  
**Kind**: property

The button’s state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var state: NSControl.StateValue { get set }
```

#### Discussion

The value of this property represents the button’s state. A button can have two or three states.  If it has two, this value is either on (`NSOnState`) or off (`NSOffState`). If it has three, this value is on, off, or mixed (`NSMixedState`). A three-state button can be enabled by calling the [`allowsMixedState`](nsbutton/allowsmixedstate.md) method. On and off states (also referred to as alternate and normal) indicate that the button is either clicked or not clicked. Mixed state is typically used for checkboxes or radio buttons, which allow for an additional intermediate state. For example, suppose the state of a checkbox is used to denote whether a text field contains bold text. If all of the text in the text field is bold, then the checkbox appears checked (on). If none of the text is bold, then the checkbox appears unchecked (off). If some of the text is bold, then the checkbox contains a dash (mixed).

Note that if the button has only two states and you set the value of [`state`](nsbutton/state.md) to mixed, the button’s state changes to on. Setting this property redraws the button, if necessary.

Although using the enumerated constants is preferred, you can also set [`state`](nsbutton/state.md) to an integer value. If the button has two states, `0` is treated as `NSOffState`, and a nonzero value is treated as `NSOnState`. If the button has three states, `0` is treated as `NSOffState`; a negative value, as `NSMixedState`; and a positive value, as `NSOnState`.

To check whether the button uses the mixed state, use the [`allowsMixedState`](nsbutton/allowsmixedstate.md) property.

## See Also

- [var allowsMixedState: Bool](nsbutton/allowsmixedstate.md)
  A Boolean value that indicates whether the button allows a mixed state.
- [func setNextState()](nsbutton/setnextstate.md)
  Sets the button to its next state.
- [func highlight(Bool)](nsbutton/highlight(_:).md)
  Highlights (or unhighlights) the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/state)*