# constrainedHigh

**Framework**: Core Image  
**Kind**: property

Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let constrainedHigh: CIDynamicRangeOption
```

#### Discussion

For best results, images should contain `contentAverageLightLevel` metadata.

## See Also

- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Use Standard dynamic range.
- [static let high: CIDynamicRangeOption](cidynamicrangeoption/high.md)
  Use High dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/constrainedhigh)*