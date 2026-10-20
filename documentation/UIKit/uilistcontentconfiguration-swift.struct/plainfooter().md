# plainFooter()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a footer in a plain list.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0 (renamed: footer)
- iPadOS 14.0+ - Deprecated in 18.0 (renamed: footer)
- Mac Catalyst 14.0+ - Deprecated in 18.0 (renamed: footer)
- tvOS 14.0+ - Deprecated in 18.0 (renamed: footer)
- visionOS

## Declaration

```swift
static func plainFooter() -> UIListContentConfiguration
```

#### Return Value

The default configuration for a footer in a plain list.

#### Discussion

Create this configuration to update the content and styling of a footer in a table view or collection view list.

For an appearance consistent with system defaults, display your footer in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md)
- [`UICollectionLayoutListConfiguration.Appearance.plain`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md)
- [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md)

Configure the background of your footer using one of the [`UIBackgroundConfiguration`](../uibackgroundconfiguration-swift.struct.md) options below. Match the background of your footer to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listPlainHeaderFooter()`](../uibackgroundconfiguration-swift.struct/listplainheaderfooter%28%29.md) | [`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md), [`UICollectionLayoutListConfiguration.Appearance.plain`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md), [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) |

## See Also

### Creating header and footer configurations
- [static func plainHeader() -> UIListContentConfiguration](./plainheader%28%29.md)
  Creates the default configuration you use to style a header in a plain list.
- [static func groupedHeader() -> UIListContentConfiguration](./groupedheader%28%29.md)
  Creates the default configuration you use to style a header in a grouped list.
- [static func groupedFooter() -> UIListContentConfiguration](./groupedfooter%28%29.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [static func prominentInsetGroupedHeader() -> UIListContentConfiguration](./prominentinsetgroupedheader%28%29.md)
  Creates the default configuration you use to style a prominent header in an inset grouped list.
- [static func extraProminentInsetGroupedHeader() -> UIListContentConfiguration](./extraprominentinsetgroupedheader%28%29.md)
  Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [static func sidebarHeader() -> UIListContentConfiguration](./sidebarheader%28%29.md)
  Creates the default configuration you use to style a header in a sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/plainfooter())*