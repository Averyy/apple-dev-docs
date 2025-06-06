# ColorScheme

**Framework**: SwiftUI  
**Kind**: enum

The possible color schemes, corresponding to the light and dark appearances.

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
enum ColorScheme
```

#### Overview

You receive a color scheme value when you read the [`colorScheme`](environmentvalues/colorscheme.md) environment value. The value tells you if a light or dark appearance currently applies to the view. SwiftUI updates the value whenever the appearance changes, and redraws views that depend on the value. For example, the following [`Text`](text.md) view automatically updates when the user enables Dark Mode:

```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

Set a preferred appearance for a particular view hierarchy to override the user’s Dark Mode setting using the [`preferredColorScheme(_:)`](view/preferredcolorscheme(_:).md) view modifier.

## Topics

### Getting color schemes
- [ColorScheme.light](colorscheme/light.md)
  The color scheme that corresponds to a light appearance.
- [ColorScheme.dark](colorscheme/dark.md)
  The color scheme that corresponds to a dark appearance.
### Creating a color scheme
- [init?(UIUserInterfaceStyle)](colorscheme/init(_:).md)
  Creates a color scheme from its user interface style equivalent.
### Supporting types
- [struct PreferredColorSchemeKey](preferredcolorschemekey.md)
  A key for specifying the preferred color scheme.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func preferredColorScheme(ColorScheme?) -> some View](view/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [var colorScheme: ColorScheme](environmentvalues/colorscheme.md)
  The color scheme of this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorscheme)*