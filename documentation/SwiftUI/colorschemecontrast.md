# ColorSchemeContrast

**Framework**: SwiftUI  
**Kind**: enum

The contrast between the app’s foreground and background colors.

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
enum ColorSchemeContrast
```

#### Overview

You receive a contrast value when you read the [`colorSchemeContrast`](environmentvalues/colorschemecontrast.md) environment value. The value tells you if a standard or increased contrast currently applies to the view. SwiftUI updates the value whenever the contrast changes, and redraws views that depend on the value. For example, the following [`Text`](text.md) view automatically updates when the user enables increased contrast:

```swift
@Environment(\.colorSchemeContrast) private var colorSchemeContrast

var body: some View {
    Text(colorSchemeContrast == .standard ? "Standard" : "Increased")
}
```

The user sets the contrast by selecting the Increase Contrast option in Accessibility > Display in System Preferences on macOS, or Accessibility > Display & Text Size in the Settings app on iOS. Your app can’t override the user’s choice. For information about using color and contrast in your app, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility#Color-and-effects) in the Human Interface Guidelines.

## Topics

### Getting contrast options
- [ColorSchemeContrast.standard](colorschemecontrast/standard.md)
  SwiftUI displays views with standard contrast between the app’s foreground and background colors.
- [ColorSchemeContrast.increased](colorschemecontrast/increased.md)
  SwiftUI displays views with increased contrast between the app’s foreground and background colors.
### Creating a color scheme contrast
- [init?(UIAccessibilityContrast)](colorschemecontrast/init(_:).md)
  Creates a contrast from its accessibility contrast equivalent.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var colorSchemeContrast: ColorSchemeContrast](environmentvalues/colorschemecontrast.md)
  The contrast associated with the color scheme of this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorschemecontrast)*