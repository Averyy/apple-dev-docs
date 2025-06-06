# containingRegion

**Framework**: Foundation  
**Kind**: property

The region that contains this region, if any.

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
var containingRegion: Locale.Region? { get }
```

#### Discussion

The following example shows how to look up the containing region for the `US` region.

```swift
let usRegion = Locale.Region("US")
let containingRegion = usRegion.containingRegion //Identifier "021": Northern America

```

## See Also

- [var identifier: String](locale/region-swift.struct/identifier.md)
  The BCP 47 identifier of the region.
- [var continent: Locale.Region?](locale/region-swift.struct/continent.md)
  The continent that contains this region, if any.
- [var isISORegion: Bool](locale/region-swift.struct/isisoregion.md)
  A Boolean value that indicates whether the region is an ISO-defined region.
- [var subRegions: [Locale.Region]](locale/region-swift.struct/subregions.md)
  An array of all the sub-regions of the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/region-swift.struct/containingregion)*