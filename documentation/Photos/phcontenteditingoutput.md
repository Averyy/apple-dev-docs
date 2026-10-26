# PHContentEditingOutput

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHContentEditingOutput
```

```objc
@interface PHContentEditingOutput : NSObject
```

## Mentions

- [Editing Asset Content](../PhotoKit/editing-asset-content.md)
- [Creating Photo Editing Extensions](../PhotoKit/creating-photo-editing-extensions.md)
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Overview

To edit an asset’s photo or video content:

1. Fetch a [`PHAsset`](./phasset.md) object that represents the photo or video to be edited.
2. Call the asset’s [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method to retrieve a [`PHContentEditingInput`](./phcontenteditinginput.md) object. This object provides information about the asset, the asset data to be edited, and a preview image for display.
3. Apply your edits to the asset. To allow a user to continue working with the edit later (for example, to adjust the parameters of a photo filter), create a [`PHAdjustmentData`](./phadjustmentdata.md) object describing the changes.
4. Initialize a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object. For photo- or video-only assets, provide the edited content with the [`renderedContentURL`](./phcontenteditingoutput/renderedcontenturl.md) property. For Live Photo assets, create a [`PHLivePhotoEditingContext`](./phlivephotoeditingcontext.md) object to edit the Live Photo content and pass your content editing output to the [`saveLivePhoto(to:options:completionHandler:)`](./phlivephotoeditingcontext/savelivephoto%28to,options,completionhandler%29.md) method.

For all asset types, provide your adjustment data with the [`adjustmentData`](./phcontenteditingoutput/adjustmentdata.md) property of the content editing output. 5. Use a photo library change block to commit the edit. (For details, see [`PHPhotoLibrary`](./phphotolibrary.md).) In the block, create a [`PHAssetChangeRequest`](./phassetchangerequest.md) object and set its [`contentEditingOutput`](./phassetchangerequest/contenteditingoutput.md) property to the editing output that you created.

Each [`PHPhotoLibrary`](./phphotolibrary.md) `performChanges` call prompts the user for permission to edit the contents of the photo library—to edit multiple assets in one batch, create multiple [`PHAssetChangeRequest`](./phassetchangerequest.md) objects within the same change block, each with its own corresponding [`PHContentEditingOutput`](./phcontenteditingoutput.md) object.

You can also edit assets from photo editing extensions. In this case, instead of working with a [`PHAsset`](./phasset.md) object, you implement methods in the [`PHContentEditingController`](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller) protocol. Photos provides a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object when your extension begins editing. When editing is complete, Photos requests a [`PHContentEditingOutput`](./phcontenteditingoutput.md) object that contains the edited asset content.

## Topics

### Creating an Output Object to Edit an Existing Asset
- [init(contentEditingInput: PHContentEditingInput)](./phcontenteditingoutput/init%28contenteditinginput%29.md)
  Creates an editing output from the specified editing input.
### Creating an Output Object to Edit a Newly Created Asset
- [init(placeholderForCreatedAsset: PHObjectPlaceholder)](./phcontenteditingoutput/init%28placeholderforcreatedasset%29.md)
  Creates an editing output for use in adding a new asset to the photo library.
### Providing Edit and Adjustment Data
- [var adjustmentData: PHAdjustmentData?](./phcontenteditingoutput/adjustmentdata.md)
  An object describing the changes made to the asset.
- [var renderedContentURL: URL](./phcontenteditingoutput/renderedcontenturl.md)
  The URL at which to write a file containing edited asset content.
### Instance Properties
- [var defaultRenderedContentType: UTType?](./phcontenteditingoutput/defaultrenderedcontenttype.md)
- [var supportedRenderedContentTypes: [UTType]](./phcontenteditingoutput/supportedrenderedcontenttypes.md)
### Instance Methods
- [func renderedContentURL(for: UTType) throws -> URL](./phcontenteditingoutput/renderedcontenturl%28for%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditingoutput)*