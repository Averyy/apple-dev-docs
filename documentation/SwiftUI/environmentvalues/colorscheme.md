# colorScheme

**Framework**: Swiftui  
**Kind**: property

The color scheme of this environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var colorScheme: ColorScheme { get set }
```

#### Discussion

Read this environment value from within a view to find out if SwiftUI is currently displaying the view using the [`ColorScheme.light`](colorscheme/light.md) or [`ColorScheme.dark`](colorscheme/dark.md) appearance. The value that you receive depends on whether the user has enabled Dark Mode, possibly superseded by the configuration of the current presentation’s view hierarchy.

```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

You can set the `colorScheme` environment value directly, but that usually isn’t what you want. Doing so changes the color scheme of the given view and its child views but  the views above it in the view hierarchy. Instead, set a color scheme using the [`preferredColorScheme(_:)`](view/preferredcolorscheme(_:).md) modifier, which also propagates the value up through the view hierarchy to the enclosing presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider also checking the [`colorSchemeContrast`](environmentvalues/colorschemecontrast.md) property, which reflects a system-wide contrast setting that the user controls. For information, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility) in the Human Interface Guidelines.

> **Note**: If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [`Asset management`](https://developer.apple.com/documentation/Xcode/asset-management).

## See Also

- [func preferredColorScheme(ColorScheme?) -> some View](view/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [enum ColorScheme](colorscheme.md)
  The possible color schemes, corresponding to the light and dark appearances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/environmentvalues/colorscheme)*