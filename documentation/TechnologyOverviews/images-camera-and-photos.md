# Images, camera, and photos

**Framework**: Technology Overviews

Display existing images and photos, create or capture new images, and read and write image data.

Include images to make your app more compelling, and effectively convey ideas and information. You can incorporate bitmap or vector-based images into your app in many ways. Use images in buttons, toolbars, and other views to reduce the amount of text in your app, which saves space and minimizes translation costs. In other parts of your interface, add images to convey ideas or add visual flair. To personalize someone’s experience, you can even incorporate images from their photo library into your interface with their permission

Build your interface from system-provided images whenever possible, and store other custom images your app requires in its bundle directory. If you create or capture new images in your app, store them in your app’s container directory or ask the person to choose a storage location.

## Choose the best file formats for images

Apple platforms support a wide assortment of image formats, including common formats like PNG, JPEG, GIF, TIFF, HEIC, camera RAW, and many others. Apple also offers SF Symbols, a library of vector- based images you can use in your apps. When creating images for your app, choose the format best suited for the intended task:

- Prefer [SF Symbols](https://developer.apple.com/sf-symbols/) for images you assign to buttons, toolbars, and other views in your interface. Symbols come in multiple weights, scale readily, and you can tint them to match your content. The SF Symbols library contains more than 6,900 symbols, and you can [create new symbols](./custom-sf-symbols.md) using the SF Symbols app.
- Use the PNG format for bitmap images you include in your interface. Apple platforms handle PNG images more efficiently than many other file formats.
- Store images you create on disk using the HEIC (High Efficiency Image Container) file format. This format offers smaller sizes than JPEG files while maintaining a high level of quality and efficiency.

One of the benefits of using Apple technologies to load images is you don’t have to know anything about the image format. The image types in [SwiftUI](../SwiftUI/image.md), [UIKit](../UIKit/uiimage.md), and [AppKit](../AppKit/nsimage.md) automatically detect image formats using a combination of filename extensions and file data, and transform the image data into a usable image object. You can read and write image data yourself if you prefer using the [Image I/O](../ImageIO/ImageIO.md) framework, but typically only do so for advanced image manipulations. For example, you might use that framework to read exposure information, timestamp details, and other image-specific metadata.

## Load images and photos from disk

The platform-provided image types handle most of the heavy lifting required to load and prepare images for display. Use the [Image](../SwiftUI/image.md), [UIImage](../UIKit/uiimage.md), and [NSImage](../AppKit/nsimage.md) types to load images from an [asset catalog](../Xcode/managing-assets-with-asset-catalogs.md), [bundle](../Foundation/bundle.md) directory, on-disk location, or from image data you create. You can also use these types to load an [SF Symbol](https://developer.apple.com/sf-symbols/) or other system-provided image. The following listing shows the code you use to create an image type and initialize it with an existing image.

**SwiftUI**:

```swift
let image = Image("MyImage")   // Load from the app bundle or an asset catalog.
let image = Image(systemName: "arrow.up")  // Load an SF Symbol.
```

**UIKit**:

```swift
let image = UIImage(named: "MyImage")  // Load from the app bundle or an asset catalog.
let image = UIImage(systemName: "arrow.up")  // Load an SF Symbol.
```

**AppKit**:

```swift
let image = NSImage(named: "MyImage")  // Load from the app bundle or an asset catalog.
let image = NSImage(systemSymbolName: "arrow.up") // Load an SF Symbol.
```

After you create an image type, display it in your app’s interface using an image view for [SwiftUI](../SwiftUI/image.md), [UIKit](../UIKit/uiimageview.md), or [AppKit](../AppKit/nsimageview.md). Although you can draw images using custom drawing code, an image view is a more efficient option and handles many types of changes for you. For example, an image view can toggle between [light and dark versions](../UIKit/providing-images-for-different-appearances.md) of an image automatically.

## Retrieve and display someone’s personal photos

People view and manage personal photos in the Photos app on their device. Apps can also request access to someone’s photos and incorporate them into the content that person creates. For example, a social media app might let someone add their personal photos to their feed. To [request access](../Photos/phphotolibrary/requestauthorization%28for,handler%29.md) and [retrieve](../PhotoKit/fetching-objects-and-requesting-changes.md) someone’s personal photos, use [PhotoKit](../PhotoKit/PhotoKit.md). You can also use PhotoKit to:

- [Create, delete, or modify](../PhotoKit/requesting-changes-to-the-photo-library.md) photos, albums, and other assets in someone’s photo library.
- [Generate thumbnail images](../Photos/phimagemanager.md) of photos in the library.
- Display motion and sound from a [Live Photo](../PhotoKit/displaying-live-photos.md) and manage playback.
- Integrate custom filter effects, slideshows, books, and other content into the Photos app using a [photo editing extension](../PhotoKit/creating-photo-editing-extensions.md).

## Capture photos and video from an available camera

Another way to integrate photos and videos into your app is to capture them using the device’s camera. On supported devices, you can display the system’s capture interface to obtain new images or video content. The interface offers a preview of the image along with controls to capture it. The use of a system-provided interface protects the person’s privacy while still giving you the images you need.

If you’re building a UIKit app, display the [image picker](../UIKit/uiimagepickercontroller.md) view controller to present the standard system interface. This interface runs out-of-process and offers options to select an existing photo or capture a new one.

When you need more control over the capture process, build a custom capture interface and use the [AVFoundation](../AVFoundation/AVFoundation.md) framework to manage the [capture process](../AVFoundation/setting-up-a-capture-session.md). Use your custom interface to capture [high-quality still images](../AVFoundation/photo-capture.md) or [audio and video](../AVFoundation/audio-and-video-capture.md), and capture content in a variety of [photo](../AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats.md) and [video](../AVFoundation/recording-movies-in-alternative-formats.md) formats. You can even capture [depth information](../AVFoundation/capturing-photos-with-depth.md) on devices that support it, and use depth values to separate foreground and background content in the image.

If you define a custom capture interface, make it more widely available by providing a [locked camera capture extension](../LockedCameraCapture/creating-a-camera-experience-for-the-lock-screen.md). This app extension is a widget that people can add to the Lock Screen, Control Center, or Action button of their iPhone or iPad. Interacting with the widget launches your app’s experience, giving them a way to capture photos and videos without navigating to your app first.

The [AVFoundation](../AVFoundation/AVFoundation.md) framework can capture content from a variety of externally connected devices, but you can also access those devices directly using the [ImageCaptureCore](../ImageCaptureCore/ImageCaptureCore.md) framework. You might use it to connect to a [camera](../ImageCaptureCore/iccameradevice.md), [scanner](../ImageCaptureCore/icscannerdevice.md), or other media device and communicate with it directly. For example, you might download existing photos and videos from the device, or use the device to capture new photos or videos.

## Read and write image data directly

For most images, you’ll use the built-in image types to load and and manage the image data. However, when you want to [read](../ImageIO/cgimagesource.md) and [write](../ImageIO/cgimagedestination.md) image data yourself, you can do so using the types of the [Image I/O](../ImageIO/ImageIO.md) framework. These types support a [wide range of image formats](../ImageIO/cgimagesourcecopytypeidentifiers%28%29.md), and make it easier to get the data you need. You can also use this framework to create [spatial photos and videos](../ImageIO/creating-spatial-photos-and-videos-with-spatial-metadata.md) for Apple Vision Pro.

Modern cameras often put metadata inside images, including exposure settings, timestamps, camera details, and even the location where the person took the picture. Use the [CGImageSource](../ImageIO/cgimagesource.md) type to retrieve this metadata as a dictionary of properties, including:

- [EXIF](../ImageIO/exif-dictionary-keys.md), [IPTC](../ImageIO/iptc-dictionary-keys.md), [GPS](../ImageIO/gps-dictionary-keys.md), and other [common image](../ImageIO/ImageIO.md) properties
- [HEIC](../ImageIO/heic-image-properties.md), [JPEG](../ImageIO/jfif-image-properties.md), [PNG](../ImageIO/png-image-properties.md), [TIFF](../ImageIO/tiff-image-properties.md), and other [format-specific](../ImageIO/ImageIO.md) data
- Manufacturer-specific data, including data from [Nikon](../ImageIO/nikon-camera-dictionary-keys.md), [Canon](../ImageIO/canon-camera-dictionary-keys.md), and [other camera types](../ImageIO/ImageIO.md)

## Create new images programmatically

In addition to using images in your interface, you can create images programmatically from your app. For example, someone using a drawing app might export an image of their artistic creation so they can share it online. A word processor app might turn someone’s document-based content into a PDF file. You might even generate images of your own app’s interface and use them in custom transition effects.

The [Core Graphics](../CoreGraphics/CoreGraphics.md) framework contains many of the fundamental types you use to generate images, and is available on all platforms. The [app-builder](./app-design-and-ui.md) frameworks also offer convenient ways to create new images. Use the following types to generate new images:

- Create an image from the content of your app’s SwiftUI views using an [ImageRenderer](../SwiftUI/imagerenderer.md) type.
- Generate an image programmatically with a [UIGraphicsImageRender](../UIKit/uigraphicsimagerenderer.md), [UIGraphicsPDFRenderer](../UIKit/uigraphicspdfrenderer.md), or [CGContext](../CoreGraphics/cgcontext.md) type.
- Build the pixel data for the image yourself and construct a new [CGImage](../CoreGraphics/cgimage.md) type with that data.
- Accelerate image-based manipulations, and apply filters and special effects to images using [Core Image](../CoreImage/CoreImage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/images-camera-and-photos)*