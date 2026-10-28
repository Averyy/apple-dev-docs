# standard

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

Use Standard dynamic range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let standard: CIDynamicRangeOption
```

```c
extern CIDynamicRangeOption const kCIDynamicRangeStandard;
```

## Discussion

Images with `contentHeadroom` metadata will be tone mapped to a maximum pixel value of 1.0.

## See Also

### Enumeration Cases
- [static let constrainedHigh: CIDynamicRangeOption](./constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [static let high: CIDynamicRangeOption](./high.md)
  Use High dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption/standard)*