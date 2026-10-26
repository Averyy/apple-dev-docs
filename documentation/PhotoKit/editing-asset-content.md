# Editing Asset Content

**Framework**: PhotoKit  
**Role**: Article

Make a request to modify and save a photo or video asset.

#### Overview

For each photo asset, Photos keeps a previous and a current version of its image data, as well as a [`PHAdjustmentData`](https://developer.apple.com/documentation/photos/phadjustmentdata) object that describes the last edit the user made to each asset’s content. Your app uses this information to support *resumable editing*.

When you begin editing an asset, Photos first asks whether your app can interpret the adjustment data from the most recent edit. If so, Photos provides the previous version of the asset as input for your editing session. After you read the adjustment data and reconstruct the edit it describes, your app might let the user alter or revert the last edit or make further changes. For example, adjustment data may describe filters applied to a photo. Your app reapplies those filters and allows the user to change filter parameters, add new filters, or remove filters.

If your app doesn’t support an asset’s adjustment data, Photos provides the current version of the asset as input to your editing session. The current version contains the rendered output of all past edits, so your app can further edit the asset but cannot alter or revert most recent edit.

To support continuity of editing between different apps and extensions, Photos keeps the current and previous versions of each asset, along with a [`PHAdjustmentData`](https://developer.apple.com/documentation/photos/phadjustmentdata) object that describes the last edit. If your app supports the adjustment data from a previous edit, you can allow the user to revert or alter the edit.

> **Note**:  For video assets, Photos doesn’t store a previous version. If your app cannot read a video asset’s adjustment data, you must work with the current version of the video. Future versions won’t be able to make use of your app’s adjustment data.

##### Request a Content Editing Input

Call the asset’s [`requestContentEditingInput(with:completionHandler:)`](https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:)) method. The [`PHContentEditingInputRequestOptions`](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions) object you provide for the `options` parameter controls whether your app can handle the asset’s adjustment data. Photos calls your `completionHandler` block, providing a [`PHContentEditingInput`](https://developer.apple.com/documentation/photos/phcontenteditinginput) object you can use for retrieving the image or video data to be edited.

##### Apply Your Edits Through a Content Editing Output

Apply your edits to the asset. To allow a user to continue working with your edits later, create a new [`PHAdjustmentData`](https://developer.apple.com/documentation/photos/phadjustmentdata) object describing the changes.

##### Create a Content Editing Output

Initialize a [`PHContentEditingOutput`](https://developer.apple.com/documentation/photos/phcontenteditingoutput) object. For photo- or video-only assets, use the editing output’s properties to provide edited asset data. For Live Photo assets, create a [`PHLivePhotoEditingContext`](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext) object to edit the Live Photo content.

##### Commit Your Completed Edits

Commit your edits to the photo library by posting a change block to the shared [`PHPhotoLibrary`](https://developer.apple.com/documentation/photos/phphotolibrary) object. In the block, create a [`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest) object and set its [`contentEditingOutput`](https://developer.apple.com/documentation/photos/phassetchangerequest/contenteditingoutput) property to the editing output that you created.

Each [`PHPhotoLibrary`](https://developer.apple.com/documentation/photos/phphotolibrary) `performChanges` call prompts the user for permission to edit the contents of the photo library. To edit multiple assets in one batch, create multiple [`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest) objects within the same change block, each with its own corresponding [`PHContentEditingOutput`](https://developer.apple.com/documentation/photos/phcontenteditingoutput) object.

## See Also

### Editing an Asset
- [class PHContentEditingInput](https://developer.apple.com/documentation/photos/phcontenteditinginput)
  A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [class PHContentEditingOutput](https://developer.apple.com/documentation/photos/phcontenteditingoutput)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](https://developer.apple.com/documentation/photos/phadjustmentdata)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [class PHLivePhotoEditingContext](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext)
  An editing session for modifying the photo, video, and audio content of a Live Photo.
- [protocol PHLivePhotoFrame](https://developer.apple.com/documentation/photos/phlivephotoframe)
  A container that provides image content for a single frame of a Live Photo in an editing context.
- [func canPerform(PHAssetEditOperation) -> Bool](https://developer.apple.com/documentation/photos/phasset/canperform(_:))
  Returns whether the asset supports the specified editing operation.
- [enum PHAssetEditOperation](https://developer.apple.com/documentation/photos/phasseteditoperation)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](https://developer.apple.com/documentation/photos/phasset/canperform(_:)) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:))
  Requests asset information for beginning a content editing session.
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](https://developer.apple.com/documentation/photos/phasset/cancelcontenteditinginputrequest(_:))
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestid)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](https://developer.apple.com/documentation/photos/phasset/originalresourcechoice-swift.enum)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](./editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:)) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/editing-asset-content)*