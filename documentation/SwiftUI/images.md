# Images

**Framework**: SwiftUI

Add images and symbols to your app’s user interface.

#### Overview

Display images, including [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols), images that you store in an asset catalog, and images that you store on disk, using an [`Image`](image.md) view.

![None](https://docs-assets.developer.apple.com/published/4fb32811fff960a104407b1f3b81a0f0/images-hero%402x.png)

For images that take time to retrieve — for example, when you load an image from a network endpoint — load the image asynchronously using [`AsyncImage`](asyncimage.md). You can instruct that view to display a placeholder during the load operation.

For design guidance, see [`Images`](https://developer.apple.com/design/Human-Interface-Guidelines/images) in the Human Interface Guidelines.

## Topics

### Creating an image
- [struct Image](image.md)
  A view that displays an image.
### Configuring an image
- [Fitting images into available space](fitting-images-into-available-space.md)
  Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [var imageScale: Image.Scale](environmentvalues/imagescale.md)
  The image scale for this environment.
- [Image.Scale](image/scale.md)
  A scale to apply to vector images relative to text.
- [Image.Orientation](image/orientation.md)
  The orientation of an image.
- [Image.ResizingMode](image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.
### Loading images asynchronously
- [struct AsyncImage](asyncimage.md)
  A view that asynchronously loads and displays an image.
- [enum AsyncImagePhase](asyncimagephase.md)
  The current phase of the asynchronous image loading operation.
### Setting a symbol variant
- [func symbolVariant(SymbolVariants) -> some View](view/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [var symbolVariants: SymbolVariants](environmentvalues/symbolvariants.md)
  The symbol variant to use in this environment.
- [struct SymbolVariants](symbolvariants.md)
  A variant of a symbol.
### Managing symbol effects
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](view/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](view/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](view/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [struct SymbolEffectTransition](symboleffecttransition.md)
  Creates a transition that applies the Appear or Disappear symbol animation to symbol images within the inserted or removed view hierarchy.
### Setting symbol rendering modes
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](view/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [struct SymbolRenderingMode](symbolrenderingmode.md)
  A symbol rendering mode.
### Rendering images from views
- [class ImageRenderer](imagerenderer.md)
  An object that creates images from SwiftUI views.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/images)*