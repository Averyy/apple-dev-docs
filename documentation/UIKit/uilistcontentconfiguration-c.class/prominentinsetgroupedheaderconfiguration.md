# prominentInsetGroupedHeaderConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a prominent header in an inset grouped list.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) prominentInsetGroupedHeaderConfiguration;
```

#### Return Value

The default configuration for a prominent header in an inset grouped list.

#### Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md)
- [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md)

Configure the background of your header using one of the [`UIBackgroundConfiguration`](../uibackgroundconfiguration-c.class.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listGroupedHeaderFooterConfiguration`](../uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration.md) | [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md), [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) |

## See Also

### Creating header and footer configurations
- [+ extraProminentInsetGroupedHeaderConfiguration](./extraprominentinsetgroupedheaderconfiguration.md)
  Creates the default configuration you use to style an extra prominent header in an inset grouped list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/prominentinsetgroupedheaderconfiguration)*