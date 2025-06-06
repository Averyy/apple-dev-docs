# accentColor

**Framework**: SwiftUI  
**Kind**: property

A color that reflects the accent color of the system or app.

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
static var accentColor: Color { get }
```

#### Discussion

The accent color is a broad theme color applied to views and controls. You can set it at the application level by specifying an accent color in your app’s asset catalog.

> **Note**: In macOS, SwiftUI applies customization of the accent color only if the user chooses Multicolor under General > Accent color in System Preferences.

In macOS, SwiftUI applies customization of the accent color only if the user chooses Multicolor under General > Accent color in System Preferences.

The following code renders a [`Text`](text.md) view using the app’s accent color:

```swift
Text("Accent Color")
    .foregroundStyle(Color.accentColor)
```

## See Also

- [static let primary: Color](color/primary.md)
  The color to use for primary content.
- [static let secondary: Color](color/secondary.md)
  The color to use for secondary content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/accentcolor)*