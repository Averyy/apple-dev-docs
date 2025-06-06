# continent

**Framework**: Foundation  
**Kind**: property

The continent that contains this region, if any.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var continent: Locale.Region? { get }
```

#### Discussion

This value can be `nil` when the system can’t determine the appropriate continent, such as when the region isn’t an ISO region.

## See Also

- [var identifier: String](locale/region-swift.struct/identifier.md)
  The BCP 47 identifier of the region.
- [var containingRegion: Locale.Region?](locale/region-swift.struct/containingregion.md)
  The region that contains this region, if any.
- [var isISORegion: Bool](locale/region-swift.struct/isisoregion.md)
  A Boolean value that indicates whether the region is an ISO-defined region.
- [var subRegions: [Locale.Region]](locale/region-swift.struct/subregions.md)
  An array of all the sub-regions of the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/region-swift.struct/continent)*