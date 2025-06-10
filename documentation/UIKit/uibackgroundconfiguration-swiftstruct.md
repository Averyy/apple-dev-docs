# UIBackgroundConfiguration

**Framework**: UIKit  
**Kind**: struct

A configuration that describes a specific background appearance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UIBackgroundConfiguration
```

#### Overview

Background configurations provide a lightweight way for you to create backgrounds for your views. Using a background configuration, you can obtain system default background styling for a variety of different view states. You apply background configurations directly to [`UIButton`](uibutton.md) or to cells, headers, and footers in [`UICollectionView`](uicollectionview.md) and [`UITableView`](uitableview.md).

To use a background configuration:

1. Create a background configuration with one of the default system styles.
2. Modify the configuration to match your view’s style if you need additional customization.
3. Set the view’s current background configuration to your configuration.

```swift
var backgroundConfig = UIBackgroundConfiguration.listPlainCell()

// Set a nil background color to use the view's tint color. 
backgroundConfig.backgroundColor = nil 

cell.backgroundConfiguration = backgroundConfig
```

You can also start by creating an empty background configuration using `clear()`, which produces a transparent background.

Each of the system background styles provides system default values for different configuration states ([`UIConfigurationState`](uiconfigurationstate-8d7pd.md)). If you apply a background configuration to a view whose [`automaticallyUpdatesBackgroundConfiguration`](uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md) property is [`true`](https://developer.apple.com/documentation/swift/true), the system automatically updates the background configuration when the view’s state changes.

If you want additional customization beyond the system default values, you can choose to manually update the background configuration by overriding the view’s [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) method.

```swift
override func updateConfiguration(using state: UIConfigurationState) {
    // Get the system default background configuration for a plain style list cell in the current state. 
    var backgroundConfig = UIBackgroundConfiguration.listPlainCell().updated(for: state) 

    // Customize the background color to use the tint color when the cell is highlighted or selected. 
     if state.isHighlighted || state.isSelected { 
        backgroundConfig.backgroundColor = nil 
     } 

    // Apply the background configuration to the cell. 
    self.backgroundConfiguration = backgroundConfig 
} 
```

When you apply a configuration to a view, UIKit performs the actual drawing and rendering of the background. When you use background configurations instead of rendering your own backgrounds, the system provides automatic view hierarchy management, support for interactive and interruptible animations and transitions, and performance optimizations.

## Topics

### Creating cell background configurations
- [static func listPlainCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listplaincell.md)
  Creates the default configuration you use to style a cell in a plain list.
- [static func listGroupedCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listgroupedcell.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [static func listSidebarCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listsidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func listAccompaniedSidebarCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listaccompaniedsidebarcell.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
### Creating header and footer background configurations
- [static func listPlainHeaderFooter() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listplainheaderfooter.md)
  Creates the default configuration you use to style a plain list header or footer.
- [static func listGroupedHeaderFooter() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listgroupedheaderfooter.md)
  Creates the default configuration you use to style a grouped list header or footer.
- [static func listSidebarHeader() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listsidebarheader.md)
  Creates the default configuration you use to style a sidebar list header.
### Creating an empty background configuration
- [static func clear() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/clear.md)
  Creates an empty background configuration with a transparent background and no default styling.
### Customizing the background
- [var customView: UIView?](uibackgroundconfiguration-swift.struct/customview.md)
  A custom view for the background.
- [var cornerRadius: CGFloat](uibackgroundconfiguration-swift.struct/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [var backgroundInsets: NSDirectionalEdgeInsets](uibackgroundconfiguration-swift.struct/backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [var edgesAddingLayoutMarginsToBackgroundInsets: NSDirectionalRectEdge](uibackgroundconfiguration-swift.struct/edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [var backgroundColor: UIColor?](uibackgroundconfiguration-swift.struct/backgroundcolor.md)
  The color of the background.
- [var backgroundColorTransformer: UIConfigurationColorTransformer?](uibackgroundconfiguration-swift.struct/backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [func resolvedBackgroundColor(for: UIColor) -> UIColor](uibackgroundconfiguration-swift.struct/resolvedbackgroundcolor(for:).md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [var visualEffect: UIVisualEffect?](uibackgroundconfiguration-swift.struct/visualeffect.md)
  The visual effect that the configuration applies to the background.
- [var shadowProperties: UIShadowProperties](uibackgroundconfiguration-swift.struct/shadowproperties.md)
- [struct UIShadowProperties](uishadowproperties-swift.struct.md)
- [var strokeColor: UIColor?](uibackgroundconfiguration-swift.struct/strokecolor.md)
  The color of the stroke.
- [var strokeColorTransformer: UIConfigurationColorTransformer?](uibackgroundconfiguration-swift.struct/strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [func resolvedStrokeColor(for: UIColor) -> UIColor](uibackgroundconfiguration-swift.struct/resolvedstrokecolor(for:).md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [var strokeWidth: CGFloat](uibackgroundconfiguration-swift.struct/strokewidth.md)
  The width of the stroke.
- [var strokeOutset: CGFloat](uibackgroundconfiguration-swift.struct/strokeoutset.md)
  The outset (or inset, if negative) for the stroke.
- [var image: UIImage?](uibackgroundconfiguration-swift.struct/image.md)
  The image displayed in the view’s background.
- [var imageContentMode: UIView.ContentMode](uibackgroundconfiguration-swift.struct/imagecontentmode.md)
  A property that determines the layout of a background image in a view when its bounds change.
### Updating background configurations
- [func updated(for: any UIConfigurationState) -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/updated(for:).md)
  Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.
### Type Methods
- [static func listCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listcell.md)
- [static func listFooter() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listfooter.md)
- [static func listHeader() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listheader.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct)*