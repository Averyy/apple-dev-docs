# PHLivePhotoEditingContext

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An editing session for modifying the photo, video, and audio content of a Live Photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHLivePhotoEditingContext
```

```objc
@interface PHLivePhotoEditingContext : NSObject
```

## Mentions

- [Editing Asset Content](../PhotoKit/editing-asset-content.md)

#### Overview

A Live Photo is a picture, captured by a supported iOS device, that includes motion and sound from the moments just before and after it was taken. Editing the content of a Live Photo works much like editing other asset types:

1. In an app using the Photos framework, fetch a [`PHAsset`](./phasset.md) object that represents the Live Photo to edit, and use that object’s [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method to retrieve a [`PHContentEditingInput`](./phcontenteditinginput.md) object.

In a photo editing extension that runs within the Photos app, your extension’s main view controller (which adopts the [`PHContentEditingController`](../PhotosUI/phcontenteditingcontroller.md) protocol) receives a [`PHContentEditingInput`](./phcontenteditinginput.md) object when the user chooses to edit a Live Photo with your extension. 2. Create a Live Photo editing context with the [`init(livePhotoEditingInput:)`](./phlivephotoeditingcontext/init%28livephotoeditinginput%29.md) initializer.

You can create a Live Photo editing context only from [`PHContentEditingInput`](./phcontenteditinginput.md) object that represents a Live Photo. Use the [`livePhoto`](./phcontenteditinginput/livephoto.md) property of the editing input to verify that it has live Photo content. 3. Use the [`frameProcessor`](./phlivephotoeditingcontext/frameprocessor.md) property to define a block to be used in processing the Live Photo’s visual content. Photos will call this block repeatedly to process each frame of the Live Photo’s video and still photo content. 4. Create a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object to store the results of your edit, then call the [`saveLivePhoto(to:options:completionHandler:)`](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md) to process the Live Photo and save it to your editing output object. This method applies your [`frameProcessor`](./phlivephotoeditingcontext/frameprocessor.md) to each frame.

> **Note**:  You can also use the [`prepareLivePhotoForPlayback(withTargetSize:options:completionHandler:)`](./phlivephotoeditingcontext/preparelivephotoforplayback%28withtargetsize,options,completionhandler%29.md) method to process a preview-quality version of the Live Photo to display in your app’s UI during editing.

1. To allow a user to continue working with the edit later (for example, to adjust the parameters of a filter), create a [`PHAdjustmentData`](./phadjustmentdata.md) object describing your changes, and store it in the [`adjustmentData`](./phcontenteditingoutput/adjustmentdata.md) property of your editing output.
2. In an app using the Photos framework, use a photo library change block to commit the edit. (For details, see [`PHPhotoLibrary`](./phphotolibrary.md).) In the block, create a [`PHAssetChangeRequest`](./phassetchangerequest.md) object and set its [`contentEditingOutput`](./phassetchangerequest/contenteditingoutput.md) property to the editing output that you created.

In a photo editing extension, provide the [`PHContentEditingOutput`](./phcontenteditingoutput.md) object that you created in your main view controller’s [`finishContentEditing(completionHandler:)`](../PhotosUI/phcontenteditingcontroller/finishcontentediting%28completionhandler%29.md) method.

When you use either of the methods listed in Processing an Editing Context’s Live Photo, Photos calls your [`frameProcessor`](./phlivephotoeditingcontext/frameprocessor.md) block repeatedly to process each frame of the Live Photo’s video and still photo content. In that block, a [`PHLivePhotoFrame`](./phlivephotoframe.md) object provides the Live Photo’s existing content as a [`CIImage`](../CoreImage/ciimage.md) object. You use Core Image to modify the image, then provide the result of your edits by returning a [`CIImage`](../CoreImage/ciimage.md) object representing the result of processing the input image.

> 💡 **Tip**:  Core Image provides several ways to process the Live Photo’s visual content. You can use the built-in filters listed in [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346) or create [`CIFilter`](../CoreImage/cifilter-swift.class.md) subclasses using custom graphics kernel code. Or, to use other image processing technologies, you can directly access and modify image content in pixel buffers, Metal textures, or `IOSurfaceRef` objects with a custom [`CIImageProcessorKernel`](../CoreImage/ciimageprocessorkernel.md) subclass.

## Topics

### Creating a Live Photo Editing Context
- [init?(livePhotoEditingInput: PHContentEditingInput)](./phlivephotoeditingcontext/init%28livephotoeditinginput%29.md)
  Creates a Live Photo editing context for the specified editing input.
### Preparing an Editing Context for Processing
- [var frameProcessor: PHLivePhotoFrameProcessingBlock?](./phlivephotoeditingcontext/frameprocessor.md)
  A block to be called by Photos for processing each frame of the Live Photo’s visual content.
- [typealias PHLivePhotoFrameProcessingBlock](./phlivephotoframeprocessingblock.md)
  The signature for a block Photos calls to process Live Photo frames.
- [var audioVolume: Float](./phlivephotoeditingcontext/audiovolume.md)
  The audio gain to apply to the processed Live Photo.
### Processing an Editing Context’s Live Photo
- [func saveLivePhoto(to: PHContentEditingOutput, options: [String : Any]?, completionHandler: (Bool, (any Error)?) -> Void)](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md)
  Processes and saves a full-quality Live Photo as the output of your editing session.
- [func prepareLivePhotoForPlayback(withTargetSize: CGSize, options: [String : Any]?, completionHandler: (PHLivePhoto?, (any Error)?) -> Void)](./phlivephotoeditingcontext/preparelivephotoforplayback%28withtargetsize,options,completionhandler%29.md)
  Processes a Live Photo with your edits for viewing.
- [struct PHLivePhotoEditingOption](./phlivephotoeditingoption.md)
  Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [func cancel()](./phlivephotoeditingcontext/cancel%28%29.md)
  Aborts any Live Photo processing in progress.
### Examining an Editing Context’s Live Photo
- [var fullSizeImage: CIImage](./phlivephotoeditingcontext/fullsizeimage.md)
  The unedited still photo content of the Live Photo.
- [var duration: CMTime](./phlivephotoeditingcontext/duration.md)
  The duration, in seconds, of the Live Photo.
- [var photoTime: CMTime](./phlivephotoeditingcontext/phototime.md)
  The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.
- [var orientation: CGImagePropertyOrientation](./phlivephotoeditingcontext/orientation.md)
  The image orientation of the Live Photo.
### Errors
- [let PHLivePhotoEditingErrorDomain: String](./phlivephotoeditingerrordomain.md)
  The domain value for error objects produced by a Live Photo editing context.
- [enum PHLivePhotoEditingErrorCode](./phlivephotoeditingerrorcode.md)
  Error codes for Live Photo editing errors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Editing an Asset
- [Editing Asset Content](../PhotoKit/editing-asset-content.md)
  Make a request to modify and save a photo or video asset.
- [class PHContentEditingInput](./phcontenteditinginput.md)
  A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [class PHContentEditingOutput](./phcontenteditingoutput.md)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](./phadjustmentdata.md)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](./phcontenteditinginputrequestoptions.md)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [protocol PHLivePhotoFrame](./phlivephotoframe.md)
  A container that provides image content for a single frame of a Live Photo in an editing context.
- [func canPerform(PHAssetEditOperation) -> Bool](./phasset/canperform%28_%29.md)
  Returns whether the asset supports the specified editing operation.
- [enum PHAssetEditOperation](./phasseteditoperation.md)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](./phasset/canperform%28_%29.md) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](./phasset/requestcontenteditinginput%28with,completionhandler%29.md)
  Requests asset information for beginning a content editing session.
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](./phasset/cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](./phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](./phasset/originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext)*