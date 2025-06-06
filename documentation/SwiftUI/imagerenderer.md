# ImageRenderer

**Framework**: SwiftUI  
**Kind**: class

An object that creates images from SwiftUI views.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final class ImageRenderer<Content> where Content : View
```

#### Overview

Use `ImageRenderer` to export bitmap image data from a SwiftUI view. You initialize the renderer with a view, then render images on demand, either by calling the [`render(rasterizationScale:renderer:)`](imagerenderer/render(rasterizationscale:renderer:).md) method, or by using the renderer’s properties to create a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage), [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage), or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage).

By drawing to a [`Canvas`](canvas.md) and exporting with an `ImageRenderer`, you can generate images from any progammatically-rendered content, like paths, shapes, gradients, and more. You can also render standard SwiftUI views like [`Text`](text.md) views, or containers of multiple view types.

The following example uses a private `createAwardView(forUser:date:)` method to create a game app’s view of a trophy symbol with a user name and date. This view combines a [`Canvas`](canvas.md) that applies a shadow filter with two [`Text`](text.md) views into a [`VStack`](vstack.md). A [`Button`](button.md) allows the person to save this view. The button’s action uses an `ImageRenderer` to rasterize a `CGImage` and then calls a private `uploadAchievementImage(_:)` method to encode and upload the image.

```swift
var body: some View {
    let trophyAndDate = createAwardView(forUser: playerName,
                                         date: achievementDate)
    VStack {
        trophyAndDate
        Button("Save Achievement") {
            let renderer = ImageRenderer(content: trophyAndDate)
            if let image = renderer.cgImage {
                uploadAchievementImage(image)
            }
        }
    }
}

private func createAwardView(forUser: String, date: Date) -> some View {
    VStack {
        Image(systemName: "trophy")
            .resizable()
            .frame(width: 200, height: 200)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .shadow(color: .mint, radius: 5)
        Text(playerName)
            .font(.largeTitle)
        Text(achievementDate.formatted())
    }
    .multilineTextAlignment(.center)
    .frame(width: 200, height: 290)
}
```

![A large trophy symbol, drawn with a mint-colored shadow. Below this, a](https://docs-assets.developer.apple.com/published/a3dc31cb9f305a02b0b44e7d8e4693e8/ImageRenderer-1%402x.png)

Because `ImageRenderer` conforms to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject), you can use it to produce a stream of images as its properties change. Subscribe to the renderer’s [`objectWillChange`](imagerenderer/objectwillchange.md) publisher, then use the renderer to rasterize a new image each time the subscriber receives an update.

> ❗ **Important**: `ImageRenderer` output only includes views that SwiftUI renders, such as text, images, shapes, and composite views of these types. It does not render views provided by native platform frameworks (AppKit and UIKit) such as web views, media players, and some controls. For these views, `ImageRenderer` displays a placeholder image, similar to the behavior of [`drawingGroup(opaque:colorMode:)`](view/drawinggroup(opaque:colormode:).md).

`ImageRenderer` output only includes views that SwiftUI renders, such as text, images, shapes, and composite views of these types. It does not render views provided by native platform frameworks (AppKit and UIKit) such as web views, media players, and some controls. For these views, `ImageRenderer` displays a placeholder image, similar to the behavior of [`drawingGroup(opaque:colorMode:)`](view/drawinggroup(opaque:colormode:).md).

##### Rendering to a Pdf Context

The [`render(rasterizationScale:renderer:)`](imagerenderer/render(rasterizationscale:renderer:).md) method renders the specified view to any [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext). That means you aren’t limited to creating a rasterized `CGImage`. For example, you can generate PDF data by rendering to a PDF context. The resulting PDF maintains resolution-independence for supported members of the view hierarchy, such as text, symbol images, lines, shapes, and fills.

The following example uses the `createAwardView(forUser:date:)` method from the previous example, and exports its contents as an 800-by-600 point PDF to the file URL `renderURL`. It uses the `size` parameter sent to the rendering closure to center the `trophyAndDate` view vertically and horizontally on the page.

```swift
var body: some View {
    let trophyAndDate = createAwardView(forUser: playerName,
                                        date: achievementDate)
    VStack {
        trophyAndDate
        Button("Save Achievement") {
            let renderer = ImageRenderer(content: trophyAndDate)
            renderer.render { size, renderer in
                var mediaBox = CGRect(origin: .zero,
                                      size: CGSize(width: 800, height: 600))
                guard let consumer = CGDataConsumer(url: renderURL as CFURL),
                      let pdfContext =  CGContext(consumer: consumer,
                                                  mediaBox: &mediaBox, nil)
                else {
                    return
                }
                pdfContext.beginPDFPage(nil)
                pdfContext.translateBy(x: mediaBox.size.width / 2 - size.width / 2,
                                       y: mediaBox.size.height / 2 - size.height / 2)
                renderer(pdfContext)
                pdfContext.endPDFPage()
                pdfContext.closePDF()
            }
        }
    }
}
```

##### Creating an Image From Drawing Instructions

`ImageRenderer` makes it possible to create a custom image by drawing into a [`Canvas`](canvas.md), rendering a `CGImage` from it, and using that to initialize an [`Image`](image.md). To simplify this process, use the `Image` initializer [`init(size:label:opaque:colorMode:renderer:)`](image/init(size:label:opaque:colormode:renderer:).md), which takes a closure whose argument is a [`GraphicsContext`](graphicscontext.md) that you can directly draw into.

## Topics

### Creating an image renderer
- [init(content: Content)](imagerenderer/init(content:).md)
  Creates a renderer object with a source content view.
### Providing the source view
- [var content: Content](imagerenderer/content.md)
  The root view rendered by this image renderer.
### Accessing renderer properties
- [var proposedSize: ProposedViewSize](imagerenderer/proposedsize.md)
  The size proposed to the root view.
- [var scale: CGFloat](imagerenderer/scale.md)
  The scale at which to render the image.
- [var isOpaque: Bool](imagerenderer/isopaque.md)
  A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [var colorMode: ColorRenderingMode](imagerenderer/colormode.md)
  The working color space and storage format of the image.
### Rendering images
- [func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) -> Void) -> Void)](imagerenderer/render(rasterizationscale:renderer:).md)
  Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [var cgImage: CGImage?](imagerenderer/cgimage.md)
  The current contents of the view, rasterized as a Core Graphics image.
- [var nsImage: NSImage?](imagerenderer/nsimage.md)
  The current contents of the view, rasterized as an AppKit image.
- [var uiImage: UIImage?](imagerenderer/uiimage.md)
  The current contents of the view, rasterized as a UIKit image.
### Producing a stream of images
- [let objectWillChange: PassthroughSubject<Void, Never>](imagerenderer/objectwillchange.md)
  A publisher that informs subscribers of changes to the image.
### Instance Properties
- [var isObservationEnabled: Bool](imagerenderer/isobservationenabled.md)
  If observers of this observed object should be notified when the produced image changes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer)*