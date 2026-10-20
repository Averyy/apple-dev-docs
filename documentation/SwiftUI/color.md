# Color

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

- [Laying out a simple view](./laying-out-a-simple-view.md)

#### Overview

You can create a color in one of several ways:

- Load a color from an Asset Catalog:

  ```swift
  let aqua = Color("aqua") // Looks in your app's main bundle by default.
  ```
- Specify component values, like red, green, and blue; hue, saturation, and brightness; or white level:

  ```swift
  let skyBlue = Color(red: 0.4627, green: 0.8392, blue: 1.0)
  let lemonYellow = Color(hue: 0.1639, saturation: 1, brightness: 1)
  let steelGray = Color(white: 0.4745)
  ```
- Create a color instance from another color, like a [`UIColor`](../UIKit/uicolor.md) or an [`NSColor`](../AppKit/nscolor.md):

  ```swift
  #if os(iOS)
  let linkColor = Color(uiColor: .link)
  #elseif os(macOS)
  let linkColor = Color(nsColor: .linkColor)
  #endif
  ```
- Use one of a palette of predefined colors, like [`black`](./shapestyle/black.md), [`green`](./shapestyle/green.md), and [`purple`](./shapestyle/purple.md).

Some view modifiers can take a color as an argument. For example, [`foregroundStyle(_:)`](./view/foregroundstyle%28_%29.md) uses the color you provide to set the foreground color for view elements, like text or [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols):

```swift
Image(systemName: "leaf.fill")
    .foregroundStyle(Color.green)
```

![A screenshot of a green leaf.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Color-1@2x.png)

Because SwiftUI treats colors as [`View`](./view.md) instances, you can also directly add them to a view hierarchy. For example, you can layer a rectangle beneath a sun image using colors defined above:

```swift
ZStack {
    skyBlue
    Image(systemName: "sun.max.fill")
        .foregroundStyle(lemonYellow)
}
.frame(width: 200, height: 100)
```

A color used as a view expands to fill all the space it’s given, as defined by the frame of the enclosing [`ZStack`](./zstack.md) in the above example:

![A screenshot of a yellow sun on a blue background.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Color-2@2x.png)

SwiftUI only resolves a color to a concrete value just before using it in a given environment. This enables a context-dependent appearance for system defined colors, or those that you load from an Asset Catalog. For example, a color can have distinct light and dark variants that the system chooses from at render time.

## Topics

### Creating a color
- [init(String, bundle: Bundle?)](./color/init%28_,bundle%29.md)
  Creates a color from a color set that you indicate by name.
- [init(_:)](./color/init%28_%29.md)
  Creates a constant color with the values specified by the resolved color.
- [func resolve(in: EnvironmentValues) -> Color.Resolved](./color/resolve%28in%29.md)
  Evaluates this color to a resolved color given the current `context`.
### Creating a color from component values
- [init(hue: Double, saturation: Double, brightness: Double, opacity: Double)](./color/init%28hue,saturation,brightness,opacity%29.md)
  Creates a constant color from hue, saturation, and brightness values.
- [init(Color.RGBColorSpace, white: Double, opacity: Double)](./color/init%28_,white,opacity%29.md)
  Creates a constant grayscale color.
- [init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double)](./color/init%28_,red,green,blue,opacity%29.md)
  Creates a constant color from red, green, and blue component values.
- [Color.RGBColorSpace](./color/rgbcolorspace.md)
  A profile that specifies how to interpret a color value for display.
### Creating a color from another color
- [init(uiColor: UIColor)](./color/init%28uicolor%29.md)
  Creates a color from a UIKit color.
- [init(nsColor: NSColor)](./color/init%28nscolor%29.md)
  Creates a color from an AppKit color.
- [init(cgColor: CGColor)](./color/init%28cgcolor%29.md)
  Creates a color from a Core Graphics color.
- [var cgColor: CGColor?](./color/cgcolor.md)
  A Core Graphics representation of the color, if available.
### Getting standard colors
- [static let black: Color](./color/black.md)
  A black color suitable for use in UI elements.
- [static let blue: Color](./color/blue.md)
  A context-dependent blue color suitable for use in UI elements.
- [static let brown: Color](./color/brown.md)
  A context-dependent brown color suitable for use in UI elements.
- [static let clear: Color](./color/clear.md)
  A clear color suitable for use in UI elements.
- [static let cyan: Color](./color/cyan.md)
  A context-dependent cyan color suitable for use in UI elements.
- [static let gray: Color](./color/gray.md)
  A context-dependent gray color suitable for use in UI elements.
- [static let green: Color](./color/green.md)
  A context-dependent green color suitable for use in UI elements.
- [static let indigo: Color](./color/indigo.md)
  A context-dependent indigo color suitable for use in UI elements.
- [static let mint: Color](./color/mint.md)
  A context-dependent mint color suitable for use in UI elements.
- [static let orange: Color](./color/orange.md)
  A context-dependent orange color suitable for use in UI elements.
- [static let pink: Color](./color/pink.md)
  A context-dependent pink color suitable for use in UI elements.
- [static let purple: Color](./color/purple.md)
  A context-dependent purple color suitable for use in UI elements.
- [static let red: Color](./color/red.md)
  A context-dependent red color suitable for use in UI elements.
- [static let teal: Color](./color/teal.md)
  A context-dependent teal color suitable for use in UI elements.
- [static let white: Color](./color/white.md)
  A white color suitable for use in UI elements.
- [static let yellow: Color](./color/yellow.md)
  A context-dependent yellow color suitable for use in UI elements.
### Getting semantic colors
- [static var accentColor: Color](./color/accentcolor.md)
  A color that reflects the accent color of the system or app.
- [static let primary: Color](./color/primary.md)
  The color to use for primary content.
- [static let secondary: Color](./color/secondary.md)
  The color to use for secondary content.
### Modifying a color
- [func opacity(Double) -> Color](./color/opacity%28_%29.md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](./color/gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](./color/mix%28with,by,in%29.md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](./color/exposureadjust%28_%29.md)
  Returns a new color with an exposure adjustment applied.
- [func headroom(Double?) -> Color](./color/headroom%28_%29.md)
  Creates a new color with specified HDR content headroom.
### Working with high dynamic range (HDR) colors
- [func resolveHDR(in: EnvironmentValues) -> Color.ResolvedHDR](./color/resolvehdr%28in%29.md)
  Evaluates this color to a resolved color with content headroom, given a set of environment values.
- [struct ResolvedHDR](./color/resolvedhdr.md)
  A concrete color value, including HDR headroom information.
### Describing a color
- [var description: String](./color/description.md)
  A textual representation of the color.
### Comparing colors
- [static func == (Color, Color) -> Bool](./color/eqeq%28_,_%29.md)
  Indicates whether two colors are equal.
- [func hash(into: inout Hasher)](./color/hash%28into%29.md)
  Hashes the essential components of the color by feeding them into the given hash function.
### Default Implementations
- [ShapeStyle Implementations](./color/shapestyle-implementations.md)
- [Transferable Implementations](./color/transferable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [ShapeStyle](./shapestyle.md)
- [Transferable](../CoreTransferable/transferable.md)
- [View](./view.md)

## See Also

### Setting a color
- [func tint(_:)](./view/tint%28_%29.md)
  Sets the tint color within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color)*