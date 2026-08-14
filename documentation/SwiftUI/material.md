# Material

**Framework**: SwiftUI  
**Kind**: struct

A background material type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Material
```

#### Overview

You can apply a blur effect to a view that appears behind another view by adding a material with the [`background(_:ignoresSafeAreaEdges:)`](view/background(_:ignoressafeareaedges:).md) modifier:

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial)
}
```

In the example above, the [`ZStack`](zstack.md) layers a [`Label`](label.md) on top of the color [`teal`](shapestyle/teal.md). The background modifier inserts the regular material below the label, blurring the part of the background that the label — including its padding — covers:

![A screenshot of a label on a teal background, where the area behind](/images/com.apple.SwiftUI/Material-1@2x.png)

A material isn’t a view, but adding a material is like inserting a translucent layer between the modified view and its background:

![An illustration that shows a background layer below a material layer,](/images/com.apple.SwiftUI/Material-2@2x.png)

The blurring effect provided by the material isn’t simple opacity. Instead, it uses a platform-specific blending that produces an effect that resembles heavily frosted glass. You can see this more easily with a complex background, like an image:

```swift
ZStack {
    Image("chili_peppers")
        .resizable()
        .aspectRatio(contentMode: .fit)
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial)
}
```

![A screenshot of a label on an image background, where the area behind](/images/com.apple.SwiftUI/Material-3@2x.png)

For physical materials, the degree to which the background colors pass through depends on the thickness. The effect also varies with light and dark appearance:

![An array of labels on a teal background. The first column, labeled light](/images/com.apple.SwiftUI/Material-4@2x.png)

If you need a material to have a particular shape, you can use the [`background(_:in:fillStyle:)`](view/background(_:in:fillstyle:).md) modifier. For example, you can create a material with rounded corners:

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 8))
}
```

![A screenshot of a label on a teal background, where the area behind](/images/com.apple.SwiftUI/Material-5@2x.png)

When you add a material, foreground elements exhibit vibrancy, a context-specific blend of the foreground and background colors that improves contrast. However using [`foregroundStyle(_:)`](view/foregroundstyle(_:).md) to set a custom foreground style — excluding the hierarchical styles, like [`secondary`](shapestyle/secondary-swift.type.property.md) — disables vibrancy.

> **Note**: A material blurs a background that’s part of your app, but not what appears behind your app on the screen. For example, the content on the Home Screen doesn’t affect the appearance of a widget.

## Topics

### Getting material types
- [static let ultraThin: Material](material/ultrathin.md)
  A mostly translucent material.
- [static let thin: Material](material/thin.md)
  A material that’s more translucent than opaque.
- [static let regular: Material](material/regular.md)
  A material that’s somewhat translucent.
- [static let thick: Material](material/thick.md)
  A material that’s more opaque than translucent.
- [static let ultraThick: Material](material/ultrathick.md)
  A mostly opaque material.
- [static let bar: Material](material/bar.md)
  A material matching the style of system toolbars.
### Instance Methods
- [func materialActiveAppearance(MaterialActiveAppearance) -> Material](material/materialactiveappearance(_:).md)
  Sets an explicit active appearance for this material.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [ShapeStyle](shapestyle.md)

## See Also

- [struct AngularGradient](angulargradient.md)
  An angular gradient.
- [struct EllipticalGradient](ellipticalgradient.md)
  A radial gradient that draws an ellipse.
- [struct LinearGradient](lineargradient.md)
  A linear gradient.
- [struct RadialGradient](radialgradient.md)
  A radial gradient.
- [struct ImagePaint](imagepaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [struct HierarchicalShapeStyle](hierarchicalshapestyle.md)
  A shape style that maps to one of the numbered content styles.
- [struct HierarchicalShapeStyleModifier](hierarchicalshapestylemodifier.md)
  Styles that you can apply to hierarchical shapes.
- [struct ForegroundStyle](foregroundstyle.md)
  The foreground style in the current context.
- [struct BackgroundStyle](backgroundstyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](selectionshapestyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](separatorshapestyle.md)
  A style appropriate for foreground separator or border lines.
- [struct TintShapeStyle](tintshapestyle.md)
  A style that reflects the current tint color.
- [struct FillShapeStyle](fillshapestyle.md)
  A shape style that displays one of the overlay fills.
- [struct LinkShapeStyle](linkshapestyle.md)
  A style appropriate for links.
- [struct PlaceholderTextShapeStyle](placeholdertextshapestyle.md)
  A style appropriate for placeholder text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/material)*