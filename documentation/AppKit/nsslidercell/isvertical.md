# isVertical

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An integer indicating the orientation (vertical or horizontal) of the slider.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var isVertical: Bool { get set }
```

```swift
var vertical: Bool { get set }
```

```objc
@property (readwrite, getter=isVertical) BOOL vertical;
```

## Discussion

The value of this property is 1 if the slider is vertical, 0 if it’s horizontal, and –1 if the orientation can’t be determined (for example, if the slider hasn’t been displayed yet). A slider is defined as vertical if its height is greater than its width.

## See Also

### Managing Cell Appearance
- [var knobThickness: CGFloat](./knobthickness.md)
  The thickness of the slider knob, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/isvertical)*