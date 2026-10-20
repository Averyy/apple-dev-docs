# warningFillColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “warning” threshold.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var warningFillColor: NSColor! { get set }
```

```objc
@property (copy, null_resettable) NSColor * warningFillColor;
```

#### Discussion

The default value is a system-defined color which may vary between level indicator styles and OS releases.

## See Also

### Configuring the Drawing Attributes
- [var ratingImage: NSImage?](./ratingimage.md)
  Sets the image used by the rating indicator style in place of the default star image.
- [var drawsTieredCapacityLevels: Bool](./drawstieredcapacitylevels.md)
- [var fillColor: NSColor!](./fillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing the “normal” state, and by the rating indicator when drawing stars.
- [var criticalFillColor: NSColor!](./criticalfillcolor.md)
  Sets the fill color used by Continuous and Discrete Capacity indicators when drawing values above the “critical” threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/warningfillcolor)*