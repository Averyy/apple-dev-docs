# ratingImage

**Framework**: AppKit  
**Kind**: property

Sets the image used by the rating indicator style in place of the default star image.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var ratingImage: NSImage? { get set }
```

#### Discussion

The default value is `nil`.

## See Also

- [var drawsTieredCapacityLevels: Bool](nslevelindicator/drawstieredcapacitylevels.md)
- [var fillColor: NSColor!](nslevelindicator/fillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing the “normal” state, and by the rating indicator when drawing stars.
- [var warningFillColor: NSColor!](nslevelindicator/warningfillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “warning” threshold.
- [var criticalFillColor: NSColor!](nslevelindicator/criticalfillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “critical” threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/ratingimage)*