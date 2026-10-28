# constrainedHigh

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

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

```c
extern CIDynamicRangeOption const kCIDynamicRangeConstrainedHigh;
```

## Discussion

For best results, images should contain `contentAverageLightLevel` metadata.

## See Also

### Enumeration Cases
- [static let standard: CIDynamicRangeOption](./standard.md)
  Use Standard dynamic range.
- [static let high: CIDynamicRangeOption](./high.md)
  Use High dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/constrainedhigh)*