# Image

**Framework**: SwiftUI  
**Kind**: struct

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

- [Building layouts with stack views](building-layouts-with-stack-views.md)
- [Fitting images into available space](fitting-images-into-available-space.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Configuring views](configuring-views.md)

#### Overview

Use an `Image` instance when you want to add images to your SwiftUI app. You can create images from many sources:

- Image files in your app’s asset library or bundle. Supported types include PNG, JPEG, HEIC, and more.
- Instances of platform-specific image types, like [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) and [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage).
- A bitmap stored in a Core Graphics [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance.
- System graphics from the SF Symbols set.

The following example shows how to load an image from the app’s asset library or bundle and scale it to fit within its container:

```swift
Image("Landscape_4")
    .resizable()
    .aspectRatio(contentMode: .fit)
Text("Water wheel")
```

![An image of a water wheel and its adjoining building, resized to fit the](https://docs-assets.developer.apple.com/published/5d218460da75fc53e2a4398f3ab30a3b/Image-1%402x.png)

You can use methods on the `Image` type as well as standard view modifiers to adjust the size of the image to fit your app’s interface. Here, the `Image` type’s [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) method scales the image to fit the current view. Then, the [`aspectRatio(_:contentMode:)`](view/aspectratio(_:contentmode:).md) view modifier adjusts this resizing behavior to maintain the image’s original aspect ratio, rather than scaling the x- and y-axes independently to fill all four sides of the view. The article [`Fitting images into available space`](fitting-images-into-available-space.md) shows how to apply scaling, clipping, and tiling to `Image` instances of different sizes.

An `Image` is a late-binding token; the system resolves its actual value only when it’s about to use the image in an environment.

##### Making Images Accessible

To use an image as a control, use one of the initializers that takes a `label` parameter. This allows the system’s accessibility frameworks to use the label as the name of the control for users who use features like VoiceOver. For images that are only present for aesthetic reasons, use an initializer with the `decorative` parameter; the accessibility systems ignore these images.

## Topics

### Creating an image
- [init(String, bundle: Bundle?)](image/init(_:bundle:).md)
  Creates a labeled image that you can use as content for controls.
- [init(String, variableValue: Double?, bundle: Bundle?)](image/init(_:variablevalue:bundle:).md)
  Creates a labeled image that you can use as content for controls, with a variable value.
- [init(ImageResource)](image/init(_:).md)
  Initialize an `Image` with an image resource.
### Creating an image for use as a control
- [init(String, bundle: Bundle?, label: Text)](image/init(_:bundle:label:).md)
  Creates a labeled image that you can use as content for controls, with the specified label.
- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](image/init(_:variablevalue:bundle:label:).md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)](image/init(_:scale:orientation:label:).md)
  Creates a labeled image based on a Core Graphics image instance, usable as content for controls.
### Creating an image for decorative use
- [init(decorative: String, bundle: Bundle?)](image/init(decorative:bundle:).md)
  Creates an unlabeled, decorative image.
- [init(decorative: String, variableValue: Double?, bundle: Bundle?)](image/init(decorative:variablevalue:bundle:).md)
  Creates an unlabeled, decorative image, with a variable value.
- [init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)](image/init(decorative:scale:orientation:).md)
  Creates an unlabeled, decorative image based on a Core Graphics image instance.
### Creating a system symbol image
- [init(systemName: String)](image/init(systemname:).md)
  Creates a system symbol image.
- [init(systemName: String, variableValue: Double?)](image/init(systemname:variablevalue:).md)
  Creates a system symbol image with a variable value.
### Creating an image from another image
- [init(uiImage: UIImage)](image/init(uiimage:).md)
  Creates a SwiftUI image from a UIKit image instance.
- [init(nsImage: NSImage)](image/init(nsimage:).md)
  Creates a SwiftUI image from an AppKit image instance.
### Creating an image from drawing instructions
- [init(size: CGSize, label: Text?, opaque: Bool, colorMode: ColorRenderingMode, renderer: (inout GraphicsContext) -> Void)](image/init(size:label:opaque:colormode:renderer:).md)
  Initializes an image of the given size, with contents provided by a custom rendering closure.
### Resizing images
- [func resizable(capInsets: EdgeInsets, resizingMode: Image.ResizingMode) -> Image](image/resizable(capinsets:resizingmode:).md)
  Sets the mode by which SwiftUI resizes an image to fit its space.
### Specifying rendering behavior
- [func antialiased(Bool) -> Image](image/antialiased(_:).md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](image/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](image/renderingmode(_:).md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](image/interpolation(_:).md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](image/templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.
- [Image.Interpolation](image/interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.
### Specifying dynamic range
- [func allowedDynamicRange(Image.DynamicRange?) -> Image](image/alloweddynamicrange(_:).md)
  Returns a new image configured with the specified allowed dynamic range.
- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [struct DynamicRange](image/dynamicrange.md)
### Instance Methods
- [func widgetAccentedRenderingMode(WidgetAccentedRenderingMode?) -> some View](image/widgetaccentedrenderingmode(_:).md)
  Specifies the how to render an `Image` when using the `WidgetKit/WidgetRenderingMode/accented` mode.
### Enumerations
- [Image.Orientation](image/orientation.md)
  The orientation of an image.
- [Image.ResizingMode](image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.
- [Image.Scale](image/scale.md)
  A scale to apply to vector images relative to text.
### Default Implementations
- [Equatable Implementations](image/equatable-implementations.md)
- [JournalingSuggestionAsset Implementations](image/journalingsuggestionasset-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [JournalingSuggestionAsset](../JournalingSuggestions/JournalingSuggestionAsset.md)
- [Sendable](../Swift/Sendable.md)
- [Transferable](../CoreTransferable/Transferable.md)
- [View](view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image)*