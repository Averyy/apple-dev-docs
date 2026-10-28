# canPerform(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns whether the asset supports the specified editing operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func canPerform(_ editOperation: PHAssetEditOperation) -> Bool
```

```objc
- (BOOL) canPerformEditOperation:(PHAssetEditOperation) editOperation;
```

## Return Value

`true` if the asset supports the specified editing operation; otherwise, `false`.

## Discussion

If an asset supports editing, you can create a [`PHAssetChangeRequest`](../phassetchangerequest.md) object inside a [`PHPhotoLibrary`](../phphotolibrary.md) change block to submit a change.

## Parameters

- `editOperation`: The operation to be tested.

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
- [enum PHAssetEditOperation](../phasseteditoperation.md)
  Values identifying possible actions an asset can support, used by the [`canPerform(_:)`](./canperform%28_%29.md) method.
- [func requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID](./requestcontenteditinginput%28with,completionhandler%29.md)
  Requests asset information for beginning a content editing session.
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](./cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](./originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](../../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./requestcontenteditinginput%28with,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/canperform(_:))*