# ratingImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the image used by the rating indicator style in place of the default star image.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var ratingImage: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * ratingImage;
```

#### Discussion

The default value is `nil`.

## See Also

### Configuring the Drawing Attributes
- [var drawsTieredCapacityLevels: Bool](./drawstieredcapacitylevels.md)
- [var fillColor: NSColor!](./fillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing the “normal” state, and by the rating indicator when drawing stars.
- [var warningFillColor: NSColor!](./warningfillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “warning” threshold.
- [var criticalFillColor: NSColor!](./criticalfillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “critical” threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/ratingimage)*