# allowsMixedState

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button allows a mixed state.

**Availability**:
- macOS

## Declaration

```swift
var allowsMixedState: Bool { get set }
```

```objc
@property BOOL allowsMixedState;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the button has three states (on, off, and mixed), or [`false`](../../Swift/false.md) if the button has two states (on and off). The default value is [`false`](../../Swift/false.md). On and off states (also referred to as alternate and normal) indicate that the button is either clicked or not clicked. Mixed state is typically used for checkboxes or radio buttons. For example, suppose the state of a checkbox is used to denote whether a text field contains bold text. If all of the text in the text field is bold, then the checkbox appears checked (on). If none of the text is bold, then the checkbox appears unchecked (off). If some of the text is bold, then the checkbox contains a dash (mixed).

## See Also

### Managing button state
- [var state: NSControl.StateValue](./state.md)
  The button’s state.
- [func setNextState()](./setnextstate%28%29.md)
  Sets the button to its next state.
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights (or unhighlights) the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/allowsmixedstate)*