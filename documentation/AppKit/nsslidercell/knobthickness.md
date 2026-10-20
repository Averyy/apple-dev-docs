# knobThickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The thickness of the slider knob, in pixels.

**Availability**:
- macOS

## Declaration

```swift
var knobThickness: CGFloat { get }
```

```objc
@property (readonly) CGFloat knobThickness;
```

#### Discussion

The thickness is defined to be the extent of the knob along the long dimension of the bar. In a vertical slider, a knob’s thickness is its height; in a horizontal slider, its thickness is its width.

## See Also

### Managing Cell Appearance
- [var isVertical: Bool](./isvertical.md)
  An integer indicating the orientation (vertical or horizontal) of the slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/knobthickness)*