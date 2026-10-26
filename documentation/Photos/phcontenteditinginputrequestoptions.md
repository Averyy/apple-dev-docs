# PHContentEditingInputRequestOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHContentEditingInputRequestOptions
```

```objc
@interface PHContentEditingInputRequestOptions : NSObject
```

## Mentions

- [Editing Asset Content](../PhotoKit/editing-asset-content.md)

#### Overview

You use the [`PHContentEditingInputRequestOptions`](./phcontenteditinginputrequestoptions.md) class with the [`requestContentEditingInput(with:completionHandler:)`](./phasset/requestcontenteditinginput%28with,completionhandler%29.md) method for editing the contents of a [`PHAsset`](./phasset.md) object.

This class doesn’t affect photo editing extensions.

## Topics

### Specifying Edting Request Options
- [var canHandleAdjustmentData: (PHAdjustmentData) -> Bool](./phcontenteditinginputrequestoptions/canhandleadjustmentdata.md)
  A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.
- [var originalResourceChoice: PHAsset.OriginalResourceChoice](./phcontenteditinginputrequestoptions/originalresourcechoice.md)
  The original resource to use as the unadjusted base when fulfilling the request.
- [var skipsDisplaySizeImage: Bool](./phcontenteditinginputrequestoptions/skipsdisplaysizeimage.md)
  Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used.
### Fetching Asset Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phcontenteditinginputrequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the asset from iCloud.
- [var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)?](./phcontenteditinginputrequestoptions/progresshandler.md)
  A block Photos calls periodically while downloading the asset.

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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions)*