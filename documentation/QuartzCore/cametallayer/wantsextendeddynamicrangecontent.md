# wantsExtendedDynamicRangeContent

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If any onscreen layer has this property set to [`true`](https://developer.apple.com/documentation/Swift/true), all rendered content is clamped to the screen’s [`maximumExtendedDynamicRangeColorComponentValue`](https://developer.apple.com/documentation/AppKit/NSScreen/maximumExtendedDynamicRangeColorComponentValue) value rather than `1.0`.

## See Also

- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](../AppKit/NSScreen/maximumExtendedDynamicRangeColorComponentValue.md)
  The current maximum color component value for the screen.
- [var edrMetadata: CAEDRMetadata?](cametallayer/edrmetadata.md)
  Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/wantsextendeddynamicrangecontent)*