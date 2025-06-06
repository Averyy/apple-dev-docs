# maximumExtendedDynamicRangeColorComponentValue

**Framework**: AppKit  
**Kind**: property

The current maximum color component value for the screen.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var maximumExtendedDynamicRangeColorComponentValue: CGFloat { get }
```

#### Discussion

If no content on screen provides extended dynamic range (EDR) values, the value of this property is `1.0`. If any content onscreen has requested EDR, the value may be greater than `1.0`, depending on the capabilities of the display hardware and other conditions. Only rendering contexts that support EDR can use values greater than `1.0`.

When the value changes, [`didChangeScreenParametersNotification`](nsapplication/didchangescreenparametersnotification.md) is posted.

## See Also

- [var wantsExtendedDynamicRangeContent: Bool { get set }](../QuartzCore/CAMetalLayer/wantsExtendedDynamicRangeContent.md)
  Enables extended dynamic range values onscreen.
- [var maximumPotentialExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumpotentialextendeddynamicrangecolorcomponentvalue.md)
  The maximum possible color component value for the screen when it’s in extended dynamic range (EDR) mode.
- [var maximumReferenceExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumreferenceextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for reference rendering to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue)*