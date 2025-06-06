# Color

**Framework**: SwiftUI  
**Kind**: struct

A representation of a color that adapts to a given context.

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
@frozen
struct Color
```

## Mentions

- [Laying out a simple view](laying-out-a-simple-view.md)

#### Overview

You can create a color in one of several ways:

- Load a color from an Asset Catalog: ```swift
let aqua = Color("aqua") // Looks in your app's main bundle by default.
```
- Specify component values, like red, green, and blue; hue, saturation, and brightness; or white level: ```swift
let skyBlue = Color(red: 0.4627, green: 0.8392, blue: 1.0)
let lemonYellow = Color(hue: 0.1639, saturation: 1, brightness: 1)
let steelGray = Color(white: 0.4745)
```
- Create a color instance from another color, like a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) or an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor): ```swift
#if os(iOS)
let linkColor = Color(uiColor: .link)
#elseif os(macOS)
let linkColor = Color(nsColor: .linkColor)
#endif
```
- Use one of a palette of predefined colors, like [`black`](shapestyle/black.md), [`green`](shapestyle/green.md), and [`purple`](shapestyle/purple.md).

Some view modifiers can take a color as an argument. For example, [`foregroundStyle(_:)`](view/foregroundstyle(_:).md) uses the color you provide to set the foreground color for view elements, like text or [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols):

```swift
Image(systemName: "leaf.fill")
    .foregroundStyle(Color.green)
```

![A screenshot of a green leaf.](https://docs-assets.developer.apple.com/published/37c0a9c2c6246f3ca18bf7f74bed4d04/Color-1%402x.png)

Because SwiftUI treats colors as [`View`](view.md) instances, you can also directly add them to a view hierarchy. For example, you can layer a rectangle beneath a sun image using colors defined above:

```swift
ZStack {
    skyBlue
    Image(systemName: "sun.max.fill")
        .foregroundStyle(lemonYellow)
}
.frame(width: 200, height: 100)
```

A color used as a view expands to fill all the space it’s given, as defined by the frame of the enclosing [`ZStack`](zstack.md) in the above example:

![A screenshot of a yellow sun on a blue background.](https://docs-assets.developer.apple.com/published/36855a93cc9257f1b96547cfd6087c28/Color-2%402x.png)

SwiftUI only resolves a color to a concrete value just before using it in a given environment. This enables a context-dependent appearance for system defined colors, or those that you load from an Asset Catalog. For example, a color can have distinct light and dark variants that the system chooses from at render time.

## Topics

### Creating a color
- [init(String, bundle: Bundle?)](color/init(_:bundle:).md)
  Creates a color from a color set that you indicate by name.
- [init(_:)](color/init(_:).md)
  Creates a constant color with the values specified by the resolved color.
- [func resolve(in: EnvironmentValues) -> Color.Resolved](color/resolve(in:).md)
  Evaluates this color to a resolved color given the current `context`.
### Creating a color from component values
- [init(hue: Double, saturation: Double, brightness: Double, opacity: Double)](color/init(hue:saturation:brightness:opacity:).md)
  Creates a constant color from hue, saturation, and brightness values.
- [init(Color.RGBColorSpace, white: Double, opacity: Double)](color/init(_:white:opacity:).md)
  Creates a constant grayscale color.
- [init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double)](color/init(_:red:green:blue:opacity:).md)
  Creates a constant color from red, green, and blue component values.
- [Color.RGBColorSpace](color/rgbcolorspace.md)
  A profile that specifies how to interpret a color value for display.
### Creating a color from another color
- [init(uiColor: UIColor)](color/init(uicolor:).md)
  Creates a color from a UIKit color.
- [init(nsColor: NSColor)](color/init(nscolor:).md)
  Creates a color from an AppKit color.
- [init(cgColor: CGColor)](color/init(cgcolor:).md)
  Creates a color from a Core Graphics color.
### Getting standard colors
- [static let black: Color](color/black.md)
  A black color suitable for use in UI elements.
- [static let blue: Color](color/blue.md)
  A context-dependent blue color suitable for use in UI elements.
- [static let brown: Color](color/brown.md)
  A context-dependent brown color suitable for use in UI elements.
- [static let clear: Color](color/clear.md)
  A clear color suitable for use in UI elements.
- [static let cyan: Color](color/cyan.md)
  A context-dependent cyan color suitable for use in UI elements.
- [static let gray: Color](color/gray.md)
  A context-dependent gray color suitable for use in UI elements.
- [static let green: Color](color/green.md)
  A context-dependent green color suitable for use in UI elements.
- [static let indigo: Color](color/indigo.md)
  A context-dependent indigo color suitable for use in UI elements.
- [static let mint: Color](color/mint.md)
  A context-dependent mint color suitable for use in UI elements.
- [static let orange: Color](color/orange.md)
  A context-dependent orange color suitable for use in UI elements.
- [static let pink: Color](color/pink.md)
  A context-dependent pink color suitable for use in UI elements.
- [static let purple: Color](color/purple.md)
  A context-dependent purple color suitable for use in UI elements.
- [static let red: Color](color/red.md)
  A context-dependent red color suitable for use in UI elements.
- [static let teal: Color](color/teal.md)
  A context-dependent teal color suitable for use in UI elements.
- [static let white: Color](color/white.md)
  A white color suitable for use in UI elements.
- [static let yellow: Color](color/yellow.md)
  A context-dependent yellow color suitable for use in UI elements.
### Getting semantic colors
- [static var accentColor: Color](color/accentcolor.md)
  A color that reflects the accent color of the system or app.
- [static let primary: Color](color/primary.md)
  The color to use for primary content.
- [static let secondary: Color](color/secondary.md)
  The color to use for secondary content.
### Modifying a color
- [func opacity(Double) -> Color](color/opacity(_:).md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](color/gradient.md)
  Returns the standard gradient for the color `self`.
### Describing a color
- [var description: String](color/description.md)
  A textual representation of the color.
### Comparing colors
- [static func == (Color, Color) -> Bool](color/==(_:_:).md)
  Indicates whether two colors are equal.
- [func hash(into: inout Hasher)](color/hash(into:).md)
  Hashes the essential components of the color by feeding them into the given hash function.
### Deprecated symbols
- [var cgColor: CGColor?](color/cgcolor.md)
  A Core Graphics representation of the color, if available.
### Instance Methods
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](color/mix(with:by:in:).md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
### Default Implementations
- [ShapeStyle Implementations](color/shapestyle-implementations.md)
- [Transferable Implementations](color/transferable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [ShapeStyle](shapestyle.md)
- [Transferable](../CoreTransferable/Transferable.md)
- [View](view.md)

## See Also

- [func tint(_:)](view/tint(_:).md)
  Sets the tint color within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color)*