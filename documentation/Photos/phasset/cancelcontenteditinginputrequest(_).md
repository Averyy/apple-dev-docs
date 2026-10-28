# cancelContentEditingInputRequest(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Cancels a request for editing the asset’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID)
```

```objc
- (void) cancelContentEditingInputRequest:(PHContentEditingInputRequestID) requestID;
```

## Discussion

When you request asset editing information with the [`requestContentEditingInput(with:completionHandler:)`](./requestcontenteditinginput%28with,completionhandler%29.md) method, the asset returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [`cancelContentEditingInputRequest(_:)`](./cancelcontenteditinginputrequest%28_%29.md) method.

## Parameters

- `requestID`: The numeric identifier of the request to be canceled.

## See Also

### Editing an Asset
- [Editing Asset Content](../../PhotoKit/editing-asset-content.md)
  Make a request to modify and save a photo or video asset.
- [class PHContentEditingInput](../phcontenteditinginput.md)
  A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [class PHContentEditingOutput](../phcontenteditingoutput.md)
  A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [class PHAdjustmentData](../phadjustmentdata.md)
  A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [class PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md)
  A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [class PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)
  An editing session for modifying the photo, video, and audio content of a Live Photo.
- [protocol PHLivePhotoFrame](../phlivephotoframe.md)
  A container that provides image content for a single frame of a Live Photo in an editing context.
- [func canPerform(PHAssetEditOperation) -> Bool](./canperform%28_%29.md)
  Returns whether the asset supports the specified editing operation.
- [enum PHAssetEditOperation](../phasseteditoperation.md)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](./canperform%28_%29.md) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](./requestcontenteditinginput%28with,completionhandler%29.md)
  Requests asset information for beginning a content editing session.
- [typealias PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](./originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](../../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./requestcontenteditinginput%28with,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/cancelcontenteditinginputrequest(_:))*