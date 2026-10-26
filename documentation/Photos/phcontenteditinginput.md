# PHContentEditingInput

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHContentEditingInput
```

```objc
@interface PHContentEditingInput : NSObject
```

## Mentions

- [Creating Photo Editing Extensions](../PhotoKit/creating-photo-editing-extensions.md)
- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)
- [Editing Asset Content](../PhotoKit/editing-asset-content.md)

#### Overview

To edit an asset’s photo or video content:

1. Fetch a [`PHAsset`](./phasset.md) object that represents the photo or video to be edited.
2. Call the asset’s [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method to retrieve a [`PHContentEditingInput`](./phcontenteditinginput.md) object.
3. Apply your edits to the asset. To allow a user to continue working with the edit later (for example, to adjust the parameters of a photo filter), create a [`PHAdjustmentData`](./phadjustmentdata.md) object describing the changes.
4. Initialize a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object. For photo- or video-only assets, use the editing output’s properties to provide edited asset data. For Live Photo assets, create a [`PHLivePhotoEditingContext`](./phlivephotoeditingcontext.md) object to edit the Live Photo content.
5. Use a photo library change block to commit the edit. In the block, create a [`PHAssetChangeRequest`](./phassetchangerequest.md) object and set its [`contentEditingOutput`](./phassetchangerequest/contenteditingoutput.md) property to the editing output that you created. For more details, see [`PHPhotoLibrary`](./phphotolibrary.md).

You can also edit assets from photo editing extensions. In this case, instead of working with a [`PHAsset`](./phasset.md) object, you implement methods in the [`PHContentEditingController`](../PhotosUI/phcontenteditingcontroller.md) protocol. Photos provides a [`PHContentEditingInput`](./phcontenteditinginput.md) object when your extension begins editing. When editing is complete, Photos requests a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object that contains the edited asset content.

## Topics

### Getting Information About the Asset
- [var mediaType: PHAssetMediaType](./phcontenteditinginput/mediatype.md)
  The type of the asset, such as video or audio.
- [enum PHAssetMediaType](./phassetmediatype.md)
  Identifies the general type of an asset, such as image or video.
- [var mediaSubtypes: PHAssetMediaSubtype](./phcontenteditinginput/mediasubtypes.md)
  The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [struct PHAssetMediaSubtype](./phassetmediasubtype.md)
  Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [var creationDate: Date?](./phcontenteditinginput/creationdate.md)
  The date and time when the asset was originally created.
- [var location: CLLocation?](./phcontenteditinginput/location.md)
  The location information that was saved with the asset.
- [var uniformTypeIdentifier: String?](./phcontenteditinginput/uniformtypeidentifier.md)
  The uniform type identifier for the asset’s image or video data.
### Working with Previous Edits
- [var adjustmentData: PHAdjustmentData?](./phcontenteditinginput/adjustmentdata.md)
  An object that describes the most recent edit to the asset’s content.
### Working with Photo Assets
- [var displaySizeImage: UIImage?](./phcontenteditinginput/displaysizeimage.md)
  An image of the asset’s contents, appropriately sized for display.
- [var fullSizeImageOrientation: Int32](./phcontenteditinginput/fullsizeimageorientation.md)
  The Exif display orientation of the full-size image file.
- [var fullSizeImageURL: URL?](./phcontenteditinginput/fullsizeimageurl.md)
  The URL to a file that contains the full-sized image data.
### Working with Video Assets
- [var audiovisualAsset: AVAsset?](./phcontenteditinginput/audiovisualasset.md)
  The video asset, as an `AVAsset` object.
- [var avAsset: AVAsset?](./phcontenteditinginput/avasset.md)
  The video asset, as an `AVAsset` object.
### Working with Live Photo Assets
- [var livePhoto: PHLivePhoto?](./phcontenteditinginput/livephoto.md)
  The unedited Live Photo content of the editing input.
- [var playbackStyle: PHAsset.PlaybackStyle](./phcontenteditinginput/playbackstyle.md)
  The style in which to present this content to the user.
- [PHAsset.PlaybackStyle](./phasset/playbackstyle-swift.enum.md)
  An enumeration of asset playback styles that dictate how to present an asset to the user.
### Instance Properties
- [var contentType: UTType?](./phcontenteditinginput/contenttype.md)
  The type of data provided as the asset’s content editing input image or video.

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
- [class PHContentEditingOutput](./phcontenteditingoutput.md)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](./phadjustmentdata.md)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](./phcontenteditinginputrequestoptions.md)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [class PHLivePhotoEditingContext](./phlivephotoeditingcontext.md)
  An editing session for modifying the photo, video, and audio content of a Live Photo.
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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput)*