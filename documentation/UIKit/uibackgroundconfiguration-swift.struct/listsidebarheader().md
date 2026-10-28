# listSidebarHeader()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a sidebar list header.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- visionOS

> **Deprecated**: Use [`listHeader()`](./listheader%28%29.md) or [`listFooter()`](./listfooter%28%29.md) instead.

## Declaration

```swift
static func listSidebarHeader() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a sidebar list header.

## Discussion

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a sidebar list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in a collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.sidebar`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) enumeration case.

## See Also

### Creating header and footer background configurations
- [static func listPlainHeaderFooter() -> UIBackgroundConfiguration](./listplainheaderfooter%28%29.md)
  Creates the default configuration you use to style a plain list header or footer.
- [static func listGroupedHeaderFooter() -> UIBackgroundConfiguration](./listgroupedheaderfooter%28%29.md)
  Creates the default configuration you use to style a grouped list header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listsidebarheader())*