# maximumPotentialExtendedDynamicRangeColorComponentValue

**Framework**: AppKit  
**Kind**: property

The maximum possible color component value for the screen when it’s in extended dynamic range (EDR) mode.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maximumPotentialExtendedDynamicRangeColorComponentValue: CGFloat { get }
```

#### Discussion

The value of this property is determined when you create the [`NSScreen`](nsscreen.md) object, and doesn’t change afterwards. If this property is greater than `1.0`, the screen supports EDR values. If the screen doesn’t support EDR values, the value is `1.0`.

The actual maximum value might be lower than this property’s value, and can change dynamically, depending on the capabilities of the display hardware and other conditions. See [`maximumExtendedDynamicRangeColorComponentValue`](nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md).

## See Also

- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for the screen.
- [var maximumReferenceExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumreferenceextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for reference rendering to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/maximumpotentialextendeddynamicrangecolorcomponentvalue)*