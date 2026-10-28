# maximumReferenceExtendedDynamicRangeColorComponentValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current maximum color component value for reference rendering to the screen.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maximumReferenceExtendedDynamicRangeColorComponentValue: CGFloat { get }
```

```objc
@property (readonly) CGFloat maximumReferenceExtendedDynamicRangeColorComponentValue;
```

## Discussion

Reference displays are calibrated to provide accurate color and lighting information that helps to optimize video content. Not all displays support reference rendering. If the display hardware doesn’t support reference rendering, the value of this property is `0`.

On reference displays, if you constrain pixel component values to values between `0` and [`maximumReferenceExtendedDynamicRangeColorComponentValue`](./maximumreferenceextendeddynamicrangecolorcomponentvalue.md), the display hardware doesn’t apply any additional tone mapping to the pixels before rendering them. If you use values above this range, display hardware may adjust content to fit into its dynamic range.

## See Also

### Getting Extended Dynamic Range Details
- [var maximumPotentialExtendedDynamicRangeColorComponentValue: CGFloat](./maximumpotentialextendeddynamicrangecolorcomponentvalue.md)
  The maximum possible color component value for the screen when it’s in extended dynamic range (EDR) mode.
- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](./maximumextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/maximumreferenceextendeddynamicrangecolorcomponentvalue)*