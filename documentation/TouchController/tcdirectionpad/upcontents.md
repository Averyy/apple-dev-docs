# upContents

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The contents for the up button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var upContents: TCControlContents? { get set }
```

```objc
@property (nonatomic, strong, nullable) TCControlContents * upContents;
```

#### Discussion

May be `nil`.

## See Also

### Inspecting the direction pad
- [var compositeLabel: TCControlLabel?](./compositelabel.md)
  A composite control label.
- [var downContents: TCControlContents?](./downcontents.md)
  The contents for the down button.
- [var downLabel: TCControlLabel?](./downlabel.md)
  The label for the down button, if the control isn’t a composite direction pad.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var inputIsMutuallyExclusive: Bool](./inputismutuallyexclusive.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var isDigital: Bool](./isdigital.md)
  A Boolean value that indicates whether the control behaves as a digital button.
- [var isRadial: Bool](./isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var leftContents: TCControlContents?](./leftcontents.md)
  The contents for the left button.
- [var leftLabel: TCControlLabel?](./leftlabel.md)
  The label for the left button, if the control isn’t a composite direction pad.
- [var rightContents: TCControlContents?](./rightcontents.md)
  The contents for the right button.
- [var rightLabel: TCControlLabel?](./rightlabel.md)
  The label for the right button, if the control isn’t a composite direction pad.
- [var upLabel: TCControlLabel?](./uplabel.md)
  The label for the up button, if the control isn’t a composite direction pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpad/upcontents)*