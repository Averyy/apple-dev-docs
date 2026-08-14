# Images, camera, and photos

**Framework**: Technology Overviews

Display existing images and photos, create or capture new images, and read and write image data.

Include images to make your app more compelling, and effectively convey ideas and information. You can incorporate bitmap or vector-based images into your app in many ways. Use images in buttons, toolbars, and other views to reduce the amount of text in your app, which saves space and minimizes translation costs. In other parts of your interface, add images to convey ideas or add visual flair. To personalize someone’s experience, you can even incorporate images from their photo library into your interface with their permission

Build your interface from system-provided images whenever possible, and store other custom images your app requires in its bundle directory. If you create or capture new images in your app, store them in your app’s container directory or ask the person to choose a storage location.

#### Choose the Best File Formats for Images

Apple platforms support a wide assortment of image formats, including common formats like PNG, JPEG, GIF, TIFF, HEIC, camera RAW, and many others. Apple also offers SF Symbols, a library of vector- based images you can use in your apps. When creating images for your app, choose the format best suited for the intended task:

- Prefer [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/) for images you assign to buttons, toolbars, and other views in your interface. Symbols come in multiple weights, scale readily, and you can tint them to match your content. The SF Symbols library contains more than 6,900 symbols, and you can [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) using the SF Symbols app.
- Use the PNG format for bitmap images you include in your interface. Apple platforms handle PNG images more efficiently than many other file formats.
- Store images you create on disk using the HEIC (High Efficiency Image Container) file format. This format offers smaller sizes than JPEG files while maintaining a high level of quality and efficiency.

One of the benefits of using Apple technologies to load images is you don’t have to know anything about the image format. The image types in [`Image`](https://developer.apple.com/documentation/swiftui/image), [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage), and [`NSImage`](https://developer.apple.com/documentation/appkit/nsimage) automatically detect image formats using a combination of filename extensions and file data, and transform the image data into a usable image object. You can read and write image data yourself if you prefer using the [`Image I/O`](https://developer.apple.com/documentation/imageio) framework, but typically only do so for advanced image manipulations. For example, you might use that framework to read exposure information, timestamp details, and other image-specific metadata.

#### Load Images and Photos From Disk

The platform-provided image types handle most of the heavy lifting required to load and prepare images for display. Use the [`Image`](https://developer.apple.com/documentation/swiftui/image), [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage), and [`NSImage`](https://developer.apple.com/documentation/appkit/nsimage) types to load images from an [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/xcode/managing-assets-with-asset-catalogs), [`Bundle`](https://developer.apple.com/documentation/foundation/bundle) directory, on-disk location, or from image data you create. You can also use these types to load an [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/) or other system-provided image. The following listing shows the code you use to create an image type and initialize it with an existing image.

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

After you create an image type, display it in your app’s interface using an image view for [`Image`](https://developer.apple.com/documentation/swiftui/image), [`UIImageView`](https://developer.apple.com/documentation/uikit/uiimageview), or [`NSImageView`](https://developer.apple.com/documentation/appkit/nsimageview). Although you can draw images using custom drawing code, an image view is a more efficient option and handles many types of changes for you. For example, an image view can toggle between [`Providing images for different appearances`](https://developer.apple.com/documentation/uikit/providing-images-for-different-appearances) of an image automatically.

#### Retrieve and Display Someones Personal Photos

People view and manage personal photos in the Photos app on their device. Apps can also request access to someone’s photos and incorporate them into the content that person creates. For example, a social media app might let someone add their personal photos to their feed. To [`requestAuthorization(for:handler:)`](https://developer.apple.com/documentation/photos/phphotolibrary/requestauthorization(for:handler:)) and [`Fetching Objects and Requesting Changes`](https://developer.apple.com/documentation/photokit/fetching-objects-and-requesting-changes) someone’s personal photos, use [`PhotoKit`](https://developer.apple.com/documentation/photokit). You can also use PhotoKit to:

- [`Requesting Changes to the Photo Library`](https://developer.apple.com/documentation/photokit/requesting-changes-to-the-photo-library) photos, albums, and other assets in someone’s photo library.
- [`PHImageManager`](https://developer.apple.com/documentation/photos/phimagemanager) of photos in the library.
- Display motion and sound from a [`Displaying Live Photos`](https://developer.apple.com/documentation/photokit/displaying-live-photos) and manage playback.
- Integrate custom filter effects, slideshows, books, and other content into the Photos app using a [`Creating Photo Editing Extensions`](https://developer.apple.com/documentation/photokit/creating-photo-editing-extensions).

#### Capture Photos and Video From an Available Camera

Another way to integrate photos and videos into your app is to capture them using the device’s camera. On supported devices, you can display the system’s capture interface to obtain new images or video content. The interface offers a preview of the image along with controls to capture it. The use of a system-provided interface protects the person’s privacy while still giving you the images you need.

If you’re building a UIKit app, display the [`UIImagePickerController`](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) view controller to present the standard system interface. This interface runs out-of-process and offers options to select an existing photo or capture a new one.

When you need more control over the capture process, build a custom capture interface and use the [`AVFoundation`](https://developer.apple.com/documentation/avfoundation) framework to manage the [`Setting up a capture session`](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session). Use your custom interface to capture [`Photo capture`](https://developer.apple.com/documentation/avfoundation/photo-capture) or [`Audio and video capture`](https://developer.apple.com/documentation/avfoundation/audio-and-video-capture), and capture content in a variety of [`Capturing photos in RAW and Apple ProRAW formats`](https://developer.apple.com/documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats) and [`Recording movies in alternative formats`](https://developer.apple.com/documentation/avfoundation/recording-movies-in-alternative-formats) formats. You can even capture [`Capturing photos with depth`](https://developer.apple.com/documentation/avfoundation/capturing-photos-with-depth) on devices that support it, and use depth values to separate foreground and background content in the image.

If you define a custom capture interface, make it more widely available by providing a [`Creating a camera experience for the Lock Screen`](https://developer.apple.com/documentation/lockedcameracapture/creating-a-camera-experience-for-the-lock-screen). This app extension is a widget that people can add to the Lock Screen, Control Center, or Action button of their iPhone or iPad. Interacting with the widget launches your app’s experience, giving them a way to capture photos and videos without navigating to your app first.

The [`AVFoundation`](https://developer.apple.com/documentation/avfoundation) framework can capture content from a variety of externally connected devices, but you can also access those devices directly using the [`ImageCaptureCore`](https://developer.apple.com/documentation/imagecapturecore) framework. You might use it to connect to a [`ICCameraDevice`](https://developer.apple.com/documentation/imagecapturecore/iccameradevice), [`ICScannerDevice`](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice), or other media device and communicate with it directly. For example, you might download existing photos and videos from the device, or use the device to capture new photos or videos.

#### Read and Write Image Data Directly

For most images, you’ll use the built-in image types to load and and manage the image data. However, when you want to [`CGImageSource`](https://developer.apple.com/documentation/imageio/cgimagesource) and [`CGImageDestination`](https://developer.apple.com/documentation/imageio/cgimagedestination) image data yourself, you can do so using the types of the [`Image I/O`](https://developer.apple.com/documentation/imageio) framework. These types support a [`CGImageSourceCopyTypeIdentifiers()`](https://developer.apple.com/documentation/imageio/cgimagesourcecopytypeidentifiers()), and make it easier to get the data you need. You can also use this framework to create [`Creating spatial photos and videos with spatial metadata`](https://developer.apple.com/documentation/imageio/creating-spatial-photos-and-videos-with-spatial-metadata) for Apple Vision Pro.

Modern cameras often put metadata inside images, including exposure settings, timestamps, camera details, and even the location where the person took the picture. Use the [`CGImageSource`](https://developer.apple.com/documentation/imageio/cgimagesource) type to retrieve this metadata as a dictionary of properties, including:

- [`EXIF Dictionary Keys`](https://developer.apple.com/documentation/imageio/exif-dictionary-keys), [`IPTC Dictionary Keys`](https://developer.apple.com/documentation/imageio/iptc-dictionary-keys), [`GPS Dictionary Keys`](https://developer.apple.com/documentation/imageio/gps-dictionary-keys), and other [`Image I/O`](https://developer.apple.com/documentation/imageio) properties
- [`HEIC Image Properties`](https://developer.apple.com/documentation/imageio/heic-image-properties), [`JFIF Image Properties`](https://developer.apple.com/documentation/imageio/jfif-image-properties), [`PNG Image Properties`](https://developer.apple.com/documentation/imageio/png-image-properties), [`TIFF Image Properties`](https://developer.apple.com/documentation/imageio/tiff-image-properties), and other [`Image I/O`](https://developer.apple.com/documentation/imageio) data
- Manufacturer-specific data, including data from [`Nikon Camera Dictionary Keys`](https://developer.apple.com/documentation/imageio/nikon-camera-dictionary-keys), [`Canon Camera Dictionary Keys`](https://developer.apple.com/documentation/imageio/canon-camera-dictionary-keys), and [`Image I/O`](https://developer.apple.com/documentation/imageio)

#### Create New Images Programmatically

In addition to using images in your interface, you can create images programmatically from your app. For example, someone using a drawing app might export an image of their artistic creation so they can share it online. A word processor app might turn someone’s document-based content into a PDF file. You might even generate images of your own app’s interface and use them in custom transition effects.

The [`Core Graphics`](https://developer.apple.com/documentation/coregraphics) framework contains many of the fundamental types you use to generate images, and is available on all platforms. The [`App design and UI`](app-design-and-ui.md) frameworks also offer convenient ways to create new images. Use the following types to generate new images:

- Create an image from the content of your app’s SwiftUI views using an [`ImageRenderer`](https://developer.apple.com/documentation/swiftui/imagerenderer) type.
- Generate an image programmatically with a [`UIGraphicsImageRenderer`](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer), [`UIGraphicsPDFRenderer`](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer), or [`CGContext`](https://developer.apple.com/documentation/coregraphics/cgcontext) type.
- Build the pixel data for the image yourself and construct a new [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage) type with that data.
- Accelerate image-based manipulations, and apply filters and special effects to images using [`Core Image`](https://developer.apple.com/documentation/coreimage).


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/images-camera-and-photos)*