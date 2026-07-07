# isDigital

**Framework**: Touch Controller  
**Kind**: property

A Boolean value that indicates whether the control behaves as a digital button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var isDigital: Bool { get set }
```

#### Discussion

If `YES`, dpad buttons will report 1 or 0. Ignored if radial is set, as button presses will always be digital.

## See Also

- [var compositeLabel: TCControlLabel?](tcdirectionpad/compositelabel.md)
  A composite control label.
- [var downContents: TCControlContents?](tcdirectionpad/downcontents.md)
  The contents for the down button.
- [var downLabel: TCControlLabel?](tcdirectionpad/downlabel.md)
  The label for the down button, if the control isn’t a composite direction pad.
- [var highlightDuration: TimeInterval](tcdirectionpad/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var inputIsMutuallyExclusive: Bool](tcdirectionpad/inputismutuallyexclusive.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var isRadial: Bool](tcdirectionpad/isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var leftContents: TCControlContents?](tcdirectionpad/leftcontents.md)
  The contents for the left button.
- [var leftLabel: TCControlLabel?](tcdirectionpad/leftlabel.md)
  The label for the left button, if the control isn’t a composite direction pad.
- [var rightContents: TCControlContents?](tcdirectionpad/rightcontents.md)
  The contents for the right button.
- [var rightLabel: TCControlLabel?](tcdirectionpad/rightlabel.md)
  The label for the right button, if the control isn’t a composite direction pad.
- [var upContents: TCControlContents?](tcdirectionpad/upcontents.md)
  The contents for the up button.
- [var upLabel: TCControlLabel?](tcdirectionpad/uplabel.md)
  The label for the up button, if the control isn’t a composite direction pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpad/isdigital)*