# sidebarHeader()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a header in a sidebar list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static func sidebarHeader() -> UIListContentConfiguration
```

#### Return Value

The default configuration for a header in a sidebar list.

#### Discussion

Create this configuration to update the content and styling of a header in a sidebar collection view list.

For an appearance consistent with system defaults, display your header in a sidebar collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.sidebar`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) enumeration case.

Configure the background of your cell using one of the [`UIBackgroundConfiguration`](uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listSidebarHeader()`](uibackgroundconfiguration-swift.struct/listsidebarheader().md) | [`UICollectionLayoutListConfiguration.Appearance.sidebar`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) |

## See Also

- [static func plainHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainheader.md)
  Creates the default configuration you use to style a header in a plain list.
- [static func plainFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainfooter.md)
  Creates the default configuration you use to style a footer in a plain list.
- [static func groupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/groupedheader.md)
  Creates the default configuration you use to style a header in a grouped list.
- [static func groupedFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/groupedfooter.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [static func prominentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader.md)
  Creates the default configuration you use to style a prominent header in an inset grouped list.
- [static func extraProminentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/extraprominentinsetgroupedheader.md)
  Creates the default configuration you use to style an extra prominent header in an inset grouped list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/sidebarheader())*