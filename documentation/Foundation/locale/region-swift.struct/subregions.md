# subRegions

**Framework**: Foundation  
**Kind**: property

An array of all the sub-regions of the region.

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
var subRegions: [Locale.Region] { get }
```

#### Discussion

The following example looks up the sub-regions of region `021`, which represents North America.

```swift
let northAmericaRegion = Locale.Region("021")
let subRegions = northAmericaRegion.subRegions //BM, CA, GL, PM, US
```

The returned `subRegions` have the following identifiers:

| Identifier | Country |
| --- | --- |
| BM | Bermuda |
| CA | Canada |
| GL | Greenland |
| PM | Saint Pierre and Miquelon |
| US | United States |

## See Also

- [var identifier: String](locale/region-swift.struct/identifier.md)
  The BCP 47 identifier of the region.
- [var containingRegion: Locale.Region?](locale/region-swift.struct/containingregion.md)
  The region that contains this region, if any.
- [var continent: Locale.Region?](locale/region-swift.struct/continent.md)
  The continent that contains this region, if any.
- [var isISORegion: Bool](locale/region-swift.struct/isisoregion.md)
  A Boolean value that indicates whether the region is an ISO-defined region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/region-swift.struct/subregions)*