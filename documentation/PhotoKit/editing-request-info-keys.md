# Editing Request Info Keys

**Framework**: PhotoKit  
**Role**: API Collection

Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:)) method.

## Topics

### Constants
- [let PHContentEditingInputResultIsInCloudKey: String](https://developer.apple.com/documentation/photos/phcontenteditinginputresultisincloudkey)
  A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [let PHContentEditingInputCancelledKey: String](https://developer.apple.com/documentation/photos/phcontenteditinginputcancelledkey)
  A Boolean value indicating whether the image request was canceled. (`NSNumber`)
- [let PHContentEditingInputErrorKey: String](https://developer.apple.com/documentation/photos/phcontenteditinginputerrorkey)
  An error that occurred while attempting to load the asset data. (`NSError`)

## See Also

### Editing an Asset
- [Editing Asset Content](./editing-asset-content.md)
  Make a request to modify and save a photo or video asset.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/editing-request-info-keys)*