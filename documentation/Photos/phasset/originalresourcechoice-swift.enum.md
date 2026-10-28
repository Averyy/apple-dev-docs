# PHAsset.OriginalResourceChoice

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

A choice of which original resource to use as the unadjusted base when reverting an asset’s content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum OriginalResourceChoice
```

```c
enum PHOriginalResourceChoice : NSInteger;
```

## Overview

Applies to RAW+JPEG assets.

## Topics

### Choices
- [PHAsset.OriginalResourceChoice.compressed](./originalresourcechoice-swift.enum/compressed.md)
  The compressed original resource, such as a JPEG or HEIC, is used.
- [PHAsset.OriginalResourceChoice.raw](./originalresourcechoice-swift.enum/raw.md)
  The RAW original resource is used.
### Initializers
- [init?(rawValue: Int)](./originalresourcechoice-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func cancelContentEditingInputRequest(PHContentEditingInputRequestID)](./cancelcontenteditinginputrequest%28_%29.md)
  Cancels a request for editing the asset’s content.
- [typealias PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md)
  An identifier for an asset content editing session.
- [Editing Request Info Keys](../../PhotoKit/editing-request-info-keys.md)
  Keys indicating the status of an asset content editing request, used in the completion handler of the [`requestContentEditingInput(with:completionHandler:)`](./requestcontenteditinginput%28with,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/originalresourcechoice-swift.enum)*