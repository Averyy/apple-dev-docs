# Editing Request Info Keys

**Framework**: PhotoKit  
**Role**: API Collection

Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](../Photos/phasset/requestcontenteditinginput%28with,completionhandler%29.md) method.

## Topics

### Constants
- [let PHContentEditingInputResultIsInCloudKey: String](../Photos/phcontenteditinginputresultisincloudkey.md)
  A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [let PHContentEditingInputCancelledKey: String](../Photos/phcontenteditinginputcancelledkey.md)
  A Boolean value indicating whether the image request was canceled. (`NSNumber`)
- [let PHContentEditingInputErrorKey: String](../Photos/phcontenteditinginputerrorkey.md)
  An error that occurred while attempting to load the asset data. (`NSError`)

## See Also

### Editing an Asset
- [Editing Asset Content](./editing-asset-content.md)
  Make a request to modify and save a photo or video asset.
- [class PHContentEditingInput](../Photos/phcontenteditinginput.md)
  A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [class PHContentEditingOutput](../Photos/phcontenteditingoutput.md)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](../Photos/phadjustmentdata.md)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](../Photos/phcontenteditinginputrequestoptions.md)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [class PHLivePhotoEditingContext](../Photos/phlivephotoeditingcontext.md)
  An editing session for modifying the photo, video, and audio content of a Live Photo.
- [protocol PHLivePhotoFrame](../Photos/phlivephotoframe.md)
  A container that provides image content for a single frame of a Live Photo in an editing context.
- [func canPerform(PHAssetEditOperation) -> Bool](../Photos/phasset/canperform%28_%29.md)
  Returns whether the asset supports the specified editing operation.
- [enum PHAssetEditOperation](../Photos/phasseteditoperation.md)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](../Photos/phasset/canperform%28_%29.md) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](../Photos/phasset/requestcontenteditinginput%28with,completionhandler%29.md)
  Requests asset information for beginning a content editing session.
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](../Photos/phasset/cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](../Photos/phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](../Photos/phasset/originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/editing-request-info-keys)*