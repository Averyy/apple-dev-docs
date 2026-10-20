# Image

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view that displays an image.

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
struct Image
```

## Mentions

- [Building layouts with stack views](./building-layouts-with-stack-views.md)
- [Configuring views](./configuring-views.md)
- [Creating performant scrollable stacks](./creating-performant-scrollable-stacks.md)
- [Displaying data in lists](./displaying-data-in-lists.md)
- [Fitting images into available space](./fitting-images-into-available-space.md)

#### Overview

Use an `Image` instance when you want to add images to your SwiftUI app. You can create images from many sources:

- Image files in your app’s asset library or bundle. Supported types include PNG, JPEG, HEIC, and more.
- Instances of platform-specific image types, like [`UIImage`](../UIKit/uiimage.md) and [`NSImage`](../AppKit/nsimage.md).
- A bitmap stored in a Core Graphics [`CGImage`](../CoreGraphics/cgimage.md) instance.
- System graphics from the SF Symbols set.

The following example shows how to load an image from the app’s asset library or bundle and scale it to fit within its container:

```swift
Image("Landscape_4")
    .resizable()
    .aspectRatio(contentMode: .fit)
Text("Water wheel")
```

![An image of a water wheel and its adjoining building, resized to fit the](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Image-1@2x.png)

You can use methods on the `Image` type as well as standard view modifiers to adjust the size of the image to fit your app’s interface. Here, the `Image` type’s [`resizable(capInsets:resizingMode:)`](./image/resizable%28capinsets,resizingmode%29.md) method scales the image to fit the current view. Then, the [`aspectRatio(_:contentMode:)`](./view/aspectratio%28_,contentmode%29.md) view modifier adjusts this resizing behavior to maintain the image’s original aspect ratio, rather than scaling the x- and y-axes independently to fill all four sides of the view. The article [Fitting images into available space](./fitting-images-into-available-space.md) shows how to apply scaling, clipping, and tiling to `Image` instances of different sizes.

An `Image` is a late-binding token; the system resolves its actual value only when it’s about to use the image in an environment.

##### Making images accessible

To use an image as a control, use one of the initializers that takes a `label` parameter. This allows the system’s accessibility frameworks to use the label as the name of the control for users who use features like VoiceOver. For images that are only present for aesthetic reasons, use an initializer with the `decorative` parameter; the accessibility systems ignore these images.

## Topics

### Creating an image
- [init(String, bundle: Bundle?)](./image/init%28_,bundle%29.md)
  Creates a labeled image that you can use as content for controls.
- [init(String, variableValue: Double?, bundle: Bundle?)](./image/init%28_,variablevalue,bundle%29.md)
  Creates a labeled image that you can use as content for controls, with a variable value.
- [init(ImageResource)](./image/init%28_%29.md)
  Initialize an `Image` with an image resource.
### Creating an image for use as a control
- [init(String, bundle: Bundle?, label: Text)](./image/init%28_,bundle,label%29.md)
  Creates a labeled image that you can use as content for controls, with the specified label.
- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](./image/init%28_,variablevalue,bundle,label%29.md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)](./image/init%28_,scale,orientation,label%29.md)
  Creates a labeled image based on a Core Graphics image instance, usable as content for controls.
### Creating an image for decorative use
- [init(decorative: String, bundle: Bundle?)](./image/init%28decorative,bundle%29.md)
  Creates an unlabeled, decorative image.
- [init(decorative: String, variableValue: Double?, bundle: Bundle?)](./image/init%28decorative,variablevalue,bundle%29.md)
  Creates an unlabeled, decorative image, with a variable value.
- [init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)](./image/init%28decorative,scale,orientation%29.md)
  Creates an unlabeled, decorative image based on a Core Graphics image instance.
### Creating a system symbol image
- [init(systemName: String)](./image/init%28systemname%29.md)
  Creates a system symbol image.
- [init(systemName: String, variableValue: Double?)](./image/init%28systemname,variablevalue%29.md)
  Creates a system symbol image with a variable value.
### Creating an image from another image
- [init(uiImage: UIImage)](./image/init%28uiimage%29.md)
  Creates a SwiftUI image from a UIKit image instance.
- [init(nsImage: NSImage)](./image/init%28nsimage%29.md)
  Creates a SwiftUI image from an AppKit image instance.
### Creating an image from drawing instructions
- [init(size: CGSize, label: Text?, opaque: Bool, colorMode: ColorRenderingMode, renderer: (inout GraphicsContext) -> Void)](./image/init%28size,label,opaque,colormode,renderer%29.md)
  Initializes an image of the given size, with contents provided by a custom rendering closure.
### Resizing images
- [func resizable(capInsets: EdgeInsets, resizingMode: Image.ResizingMode) -> Image](./image/resizable%28capinsets,resizingmode%29.md)
  Sets the mode by which SwiftUI resizes an image to fit its space.
### Specifying rendering behavior
- [func antialiased(Bool) -> Image](./image/antialiased%28_%29.md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](./image/symbolrenderingmode%28_%29.md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](./image/renderingmode%28_%29.md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](./image/interpolation%28_%29.md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](./image/templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.
- [Image.Interpolation](./image/interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.
### Specifying dynamic range
- [func allowedDynamicRange(Image.DynamicRange?) -> Image](./image/alloweddynamicrange%28_%29.md)
  Returns a new image configured with the specified allowed dynamic range.
- [var allowedDynamicRange: Image.DynamicRange?](./environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [struct DynamicRange](./image/dynamicrange.md)
  The range of brightness that an image is allowed to draw.
### Instance Methods
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> Image](./image/symbolcolorrenderingmode%28_%29.md)
  Sets the color rendering mode of the image.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> Image](./image/symbolvariablevaluemode%28_%29.md)
  Sets the variable value mode mode for symbol images within this view.
- [func widgetAccentedRenderingMode(WidgetAccentedRenderingMode?) -> some View](./image/widgetaccentedrenderingmode%28_%29.md)
  Specifies the how to render an `Image` when using the `WidgetKit/WidgetRenderingMode/accented` mode.
### Enumerations
- [Image.Orientation](./image/orientation.md)
  The orientation of an image.
- [Image.ResizingMode](./image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.
- [Image.Scale](./image/scale.md)
  A scale to apply to vector images relative to text.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [JournalingSuggestionAsset](../JournalingSuggestions/journalingsuggestionasset.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transferable](../CoreTransferable/transferable.md)
- [View](./view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image)*