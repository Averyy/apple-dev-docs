# maximumExtendedDynamicRangeColorComponentValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current maximum color component value for the screen.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var maximumExtendedDynamicRangeColorComponentValue: CGFloat { get }
```

```objc
@property (readonly) CGFloat maximumExtendedDynamicRangeColorComponentValue;
```

## Discussion

If no content on screen provides extended dynamic range (EDR) values, the value of this property is `1.0`. If any content onscreen has requested EDR, the value may be greater than `1.0`, depending on the capabilities of the display hardware and other conditions. Only rendering contexts that support EDR can use values greater than `1.0`.

When the value changes, [`didChangeScreenParametersNotification`](../nsapplication/didchangescreenparametersnotification.md) is posted.

## See Also

### Related Documentation
- [var wantsExtendedDynamicRangeContent: Bool](../../QuartzCore/cametallayer/wantsextendeddynamicrangecontent.md)
  Enables extended dynamic range values onscreen.
### Getting Extended Dynamic Range Details
- [var maximumPotentialExtendedDynamicRangeColorComponentValue: CGFloat](./maximumpotentialextendeddynamicrangecolorcomponentvalue.md)
  The maximum possible color component value for the screen when it’s in extended dynamic range (EDR) mode.
- [var maximumReferenceExtendedDynamicRangeColorComponentValue: CGFloat](./maximumreferenceextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for reference rendering to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue)*