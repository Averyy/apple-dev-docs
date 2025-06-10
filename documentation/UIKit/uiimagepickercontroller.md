# UIImagePickerController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the system interfaces for taking pictures, recording movies, and choosing items from the user’s media library.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIImagePickerController
```

#### Overview

An image picker controller manages user interactions and delivers the results of those interactions to a delegate object. The role and appearance of an image picker controller depend on the  you assign to it before you present it.

- A [`sourceType`](uiimagepickercontroller/sourcetype-swift.property.md) of [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md) provides a user interface for taking a new picture or movie (on devices that support media capture).
- A [`sourceType`](uiimagepickercontroller/sourcetype-swift.property.md) of [`UIImagePickerController.SourceType.photoLibrary`](uiimagepickercontroller/sourcetype-swift.enum/photolibrary.md) or [`UIImagePickerController.SourceType.savedPhotosAlbum`](uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum.md) provides a user interface for choosing among saved pictures and movies.

To use an image picker controller containing its default controls, perform these steps:

1. Verify that the device is capable of picking content from the desired source. Do this by calling the [`isSourceTypeAvailable(_:)`](uiimagepickercontroller/issourcetypeavailable(_:).md) class method, providing a constant from the [`UIImagePickerController.SourceType`](uiimagepickercontroller/sourcetype-swift.enum.md) enumeration.
2. Check which media types are available for the source type you’re using, by calling the [`availableMediaTypes(for:)`](uiimagepickercontroller/availablemediatypes(for:).md) class method. This lets you distinguish between a camera that can be used for video recording and one that can be used only for still images.
3. Tell the image picker controller to adjust the UI according to the media types you want to make available — still images, movies, or both — by setting the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) property.
4. Present the user interface. On iPhone or iPod touch, do this modally (full screen) by calling the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method of the currently active view controller, passing your configured image picker controller as the new view controller.

On iPad, the correct way to present an image picker depends on its source type, as summarized in this table:

| Camera | Photo Library | Saved Photos Album |
| --- | --- | --- |
| Use full screen | Must use a popover | Must use a popover |

The table indicates that on iPad, if you specify a source type of [`UIImagePickerController.SourceType.photoLibrary`](uiimagepickercontroller/sourcetype-swift.enum/photolibrary.md) or [`UIImagePickerController.SourceType.savedPhotosAlbum`](uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum.md), you must present the image picker using a popover controller (to learn how to do this, see [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md)). If you attempt to present an image picker modally (full screen) for choosing among saved pictures and movies, the system raises an exception.

On iPad, if you specify a source type of [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md), you can present the image picker modally (full screen) or by using a popover. However, Apple recommends that you present the camera interface only full screen.

1. When the user taps a button to pick a newly captured or saved image or movie, or cancels the operation, dismiss the image picker using your delegate object. For newly captured media, your delegate can then save it to the photo library on the device. For previously saved media, your delegate can then use the image data according to the purpose of your app.

For details on these steps, refer to [`Taking Pictures and Movies`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Articles/TakingPicturesAndMovies.html#//apple_ref/doc/uid/TP40010406).

You can customize an image picker controller to manage user interactions yourself. To do this, provide an overlay view containing the controls you want to display, and use the methods described in [`Capturing still images or movies`](uiimagepickercontroller#Capturing-still-images-or-movies.md). You can display your custom overlay view in addition to, or instead of, the default controls. Custom overlay views for the `UIImagePickerController` class are available in iOS 3.1 and later by way of the [`cameraOverlayView`](uiimagepickercontroller/cameraoverlayview.md) property. For a code example, see the [`Customizing an image picker controller`](customizing-an-image-picker-controller.md) sample code project.

> ❗ **Important**:  The `UIImagePickerController` class supports portrait mode only. This class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private and must not be modified, with one exception. You can assign a custom view to the [`cameraOverlayView`](uiimagepickercontroller/cameraoverlayview.md) property and use that view to present additional information or manage the interactions between the camera interface and your code.

##### Provide a Delegate Object

To use an image picker controller, you must provide a delegate that conforms to the [`UIImagePickerControllerDelegate`](uiimagepickercontrollerdelegate.md) protocol. Starting in iOS 4.1, you can use the delegate to save still-image metadata to the photo library along with the image. See [`UIImagePickerControllerDelegate`](uiimagepickercontrollerdelegate.md).

##### Observe Required Viewing Standards

As a view controller that renders on top of your app for the temporary purpose of selecting images, the picker controller expects your app to keep its contents visible as a prerequisite to operation. In iOS 17 and later, the picker controller ignores touch events while its opacity is anything other than fully opaque. If your app alters the controller’s visibility, such as by adjusting the [`opacity`](https://developer.apple.com/documentation/QuartzCore/CALayer/opacity) of its view’s layer, the picker controller disables user interaction.

##### Adjust Flash Mode

In iOS 4.0 and later, you can provide custom controls to let the user adjust flash mode (on devices that have a flash LED), pick which camera to use (on devices that have a front and rear camera), and switch between still image and movie capture. You can also manage these settings programmatically. You can also manipulate the flash directly to provide effects, such as a strobe light. Present a picker interface set to use video capture mode. Then, turn the flash LED on or off by setting the [`cameraFlashMode`](uiimagepickercontroller/cameraflashmode-swift.property.md) property to [`UIImagePickerController.CameraFlashMode.on`](uiimagepickercontroller/cameraflashmode-swift.enum/on.md) or [`UIImagePickerController.CameraFlashMode.off`](uiimagepickercontroller/cameraflashmode-swift.enum/off.md).

##### Work with Movies

Movie capture has a default duration limit of 10 minutes but can be adjusted using the [`videoMaximumDuration`](uiimagepickercontroller/videomaximumduration.md) property. When a person taps the Share button to send a movie to MMS, YouTube, or another destination, the system applies duration and video quality limitations.

The default camera interface supports editing movies in the photo library. Editing involves trimming from the start or end of the movie, then saving the trimmed movie. To display an interface dedicated to movie editing, rather than one that also supports recording new movies, use the [`UIVideoEditorController`](uivideoeditorcontroller.md) class instead of this one. See [`UIVideoEditorController`](uivideoeditorcontroller.md).

##### Work with Live Photos

Live Photos is a Camera app feature on supported devices, enabling a picture to be not just a single moment in time but to include motion and sound from the moments just before and after its capture. A [`PHLivePhoto`](https://developer.apple.com/documentation/Photos/PHLivePhoto) object represents a Live Photo, and the [`PHLivePhotoView`](https://developer.apple.com/documentation/PhotosUI/PHLivePhotoView) class provides a system-standard, interactive user interface for displaying a Live Photo and playing back its content.

Although Live Photos include sound and motion, they remain photos. When you use an image picker controller to capture or choose still images (by including only the `kUTTypeImage` type in the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) array), assets that were captured as Live Photos continue to appear in the picker. However, when the user chooses an asset, your [`delegate`](uiimagepickercontroller/delegate.md) object receives only a [`UIImage`](uiimage.md) object containing a still-image representation of the Live Photo.

To obtain the full motion and sound content when the user chooses a Live Photo with the image picker, you must include  the `kUTTypeImage` and `kUTTypeLivePhoto` types in the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) array. For more information, see [`livePhoto`](uiimagepickercontroller/infokey/livephoto.md) in [`UIImagePickerControllerDelegate`](uiimagepickercontrollerdelegate.md).

##### Perform Fully Customized Media Capture and Browsing

To perform fully customized image or movie capture, instead use the [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) framework as described in [`Still and Video Media Capture`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188-CH1-SW10). Camera access using the AVFoundation framework is available starting in iOS 4.0.

To create a fully customized image picker for browsing the photo library, use classes from the Photos framework. For example, you could create a custom image picker that displays larger thumbnail images generated and cached by iOS, that makes use of image metadata including timestamp and location information, or that integrates with other features such as MapKit and iCloud Photo Sharing. For more information, see [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit). Media browsing using the Photos framework is available starting in iOS 8.0.

## Topics

### Responding to interactions with the picker
- [var delegate: (any UIImagePickerControllerDelegate & UINavigationControllerDelegate)?](uiimagepickercontroller/delegate.md)
  The image picker’s delegate object.
- [protocol UIImagePickerControllerDelegate](uiimagepickercontrollerdelegate.md)
  A set of methods that your delegate object must implement to interact with the image picker interface.
### Setting the picker source
- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](uiimagepickercontroller/availablemediatypes(for:).md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [var sourceType: UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.property.md)
  The type of picker interface to be displayed by the controller.
- [UIImagePickerController.SourceType](uiimagepickercontroller/sourcetype-swift.enum.md)
  Constants that describe the source to use when picking an image or when determining available media types.
### Configuring the picker
- [var mediaTypes: [String]](uiimagepickercontroller/mediatypes.md)
  An array that indicates the media types to access by the media picker controller.
- [var allowsEditing: Bool](uiimagepickercontroller/allowsediting.md)
  A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.
### Configuring the video capture options
- [var videoQuality: UIImagePickerController.QualityType](uiimagepickercontroller/videoquality.md)
  The video recording and transcoding quality.
- [UIImagePickerController.QualityType](uiimagepickercontroller/qualitytype.md)
  Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.
- [var videoMaximumDuration: TimeInterval](uiimagepickercontroller/videomaximumduration.md)
  The maximum duration, in seconds, for a video recording.
### Customizing the camera controls
- [Customizing an image picker controller](customizing-an-image-picker-controller.md)
  Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [var showsCameraControls: Bool](uiimagepickercontroller/showscameracontrols.md)
  A Boolean value that indicates whether the image picker displays the default camera controls.
- [var cameraOverlayView: UIView?](uiimagepickercontroller/cameraoverlayview.md)
  The view to display on top of the default image picker interface.
- [var cameraViewTransform: CGAffineTransform](uiimagepickercontroller/cameraviewtransform.md)
  The transform to apply to the camera’s preview image.
### Capturing still images or movies
- [func takePicture()](uiimagepickercontroller/takepicture.md)
  Captures a still image using the camera.
- [func startVideoCapture() -> Bool](uiimagepickercontroller/startvideocapture.md)
  Starts video capture using the camera specified by the camera device property.
- [func stopVideoCapture()](uiimagepickercontroller/stopvideocapture.md)
  Stops video capture.
### Configuring the camera to use
- [class func isCameraDeviceAvailable(UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/iscameradeviceavailable(_:).md)
  Queries whether the specified camera is available.
- [var cameraDevice: UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.enum.md)
  Constants that specify the camera to use for image or movie capture.
### Configuring the camera capture mode
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](uiimagepickercontroller/availablecapturemodes(for:).md)
  Retrieves the capture modes supported by the specified camera device.
- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.property.md)
  The capture mode used by the camera.
- [UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.enum.md)
  Constants that specify the category of media for the camera to capture.
### Configuring the flash behavior
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/isflashavailable(for:).md)
  Queries whether the specified camera has flash illumination capability.
- [var cameraFlashMode: UIImagePickerController.CameraFlashMode](uiimagepickercontroller/cameraflashmode-swift.property.md)
  The flash mode used by the active camera.
- [UIImagePickerController.CameraFlashMode](uiimagepickercontroller/cameraflashmode-swift.enum.md)
  Constants that specify the flash mode to use with the active camera.
### Configuring the export presets
- [var imageExportPreset: UIImagePickerController.ImageURLExportPreset](uiimagepickercontroller/imageexportpreset.md)
  The preset to use when preparing images for export to your app.
- [UIImagePickerController.ImageURLExportPreset](uiimagepickercontroller/imageurlexportpreset.md)
  Constants that indicate how to export images to the client app.
- [var videoExportPreset: String](uiimagepickercontroller/videoexportpreset.md)
  The preset to use when preparing video for export to your app.

## Relationships

### Inherits From
- [UINavigationController](uinavigationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIVideoEditorController](uivideoeditorcontroller.md)
  A view controller that manages the system interface for trimming video frames and encoding a previously recorded movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)*