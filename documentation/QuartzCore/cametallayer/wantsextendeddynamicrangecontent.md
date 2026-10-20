# wantsExtendedDynamicRangeContent

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Enables extended dynamic range values onscreen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var wantsExtendedDynamicRangeContent: Bool { get set }
```

```objc
@property BOOL wantsExtendedDynamicRangeContent;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). If any onscreen layer has this property set to [`true`](../../Swift/true.md), all rendered content is clamped to the screen’s [`maximumExtendedDynamicRangeColorComponentValue`](../../AppKit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md) value rather than `1.0`.

## See Also

### Related Documentation
- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](../../AppKit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for the screen.
### Configuring Extended Dynamic Range Behavior
- [var edrMetadata: CAEDRMetadata?](./edrmetadata.md)
  Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/wantsextendeddynamicrangecontent)*