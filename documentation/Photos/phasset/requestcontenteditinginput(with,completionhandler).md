# requestContentEditingInput(with:completionHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests asset information for beginning a content editing session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestContentEditingInput(with options: PHContentEditingInputRequestOptions?, completionHandler: @escaping (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID
```

```objc
- (PHContentEditingInputRequestID) requestContentEditingInputWithOptions:(PHContentEditingInputRequestOptions *) options completionHandler:(void (^)(PHContentEditingInput *contentEditingInput, NSDictionary *info)) completionHandler;
```

## Mentions

- [Editing Asset Content](../../PhotoKit/editing-asset-content.md)

#### Return Value

A numeric identifier for the request. Pass this identifier to the [`cancelContentEditingInputRequest(_:)`](./cancelcontenteditinginputrequest%28_%29.md) method if you need to cancel the request before it completes.

#### Discussion

When you call this method, Photos downloads the asset’s image or video data (if necessary) and prepares it for editing, then calls your `completionHandler` block to provide a [`PHContentEditingInput`](../phcontenteditinginput.md) object you use for editing.

To complete the edit, create a [`PHContentEditingOutput`](../phcontenteditingoutput.md) object from the editing input to provide the edited asset data. Then, commit the edit by posting a change block to the shared [`PHPhotoLibrary`](../phphotolibrary.md) object. In the block, create a [`PHAssetChangeRequest`](../phassetchangerequest.md) object and set its [`contentEditingOutput`](../phassetchangerequest/contenteditingoutput.md) property to the editing output you created.

## Parameters

- `options`: Options affecting how Photos handles an edit session request.
- `completionHandler`: A block that Photos calls when the requested asset editing information is ready.

  The block takes the following parameters:

  - **contentEditingInput**: An object that describes the asset for editing and provides methods for loading the image or video content to be edited.
  - **info**: A dictionary providing information about the status of the request. See [Editing Request Info Keys](../../PhotoKit/editing-request-info-keys.md) for possible keys and values.

  In iOS 10.0, tvOS 10.0, and later, Photos always calls this block on the main queue. In earlier releases, Photos calls this block on an arbitrary serial queue—if your block needs to update the UI, dispatch that work to the main queue.

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
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](./cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [PHAsset.OriginalResourceChoice](./originalresourcechoice-swift.enum.md)
  A choice of which original resource to use as the unadjusted base when reverting an asset’s content.
- [Editing Request Info Keys](../../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./requestcontenteditinginput%28with,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:))*