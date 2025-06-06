# colorSchemeContrast

**Framework**: SwiftUI  
**Kind**: property

The contrast associated with the color scheme of this environment.

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
var colorSchemeContrast: ColorSchemeContrast { get }
```

#### Discussion

Read this environment value from within a view to find out if SwiftUI is currently displaying the view using [`ColorSchemeContrast.standard`](colorschemecontrast/standard.md) or [`ColorSchemeContrast.increased`](colorschemecontrast/increased.md) contrast. The value that you read depends entirely on user settings, and you can’t change it.

```swift
@Environment(\.colorSchemeContrast) private var colorSchemeContrast

var body: some View {
    Text(colorSchemeContrast == .standard ? "Standard" : "Increased")
}
```

When adjusting your app’s user interface to match the contrast, consider also checking the [`colorScheme`](environmentvalues/colorscheme.md) property to find out if SwiftUI is displaying the view with a light or dark appearance. For information, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility) in the Human Interface Guidelines.

> **Note**: If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [`Asset management`](https://developer.apple.com/documentation/Xcode/asset-management).

If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [`Asset management`](https://developer.apple.com/documentation/Xcode/asset-management).

## See Also

- [enum ColorSchemeContrast](colorschemecontrast.md)
  The contrast between the app’s foreground and background colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/colorschemecontrast)*