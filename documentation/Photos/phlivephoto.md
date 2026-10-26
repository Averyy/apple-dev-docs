# PHLivePhoto

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A displayable representation of a Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHLivePhoto
```

```objc
@interface PHLivePhoto : NSObject
```

## Mentions

- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)

#### Overview

In iOS and tvOS, you can use this class to reference Live Photos from the user’s library (fetched with the [`PHAsset`](./phasset.md) and [`PHImageManager`](./phimagemanager.md) classes), to load displayable Live Photo objects from data obtained elsewhere (such as pictures shared through a social network), and to assign Live Photos to [`PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview) objects for display.

In iOS, tvOS, and macOS, you can use this class to display edits in progress for Live Photo content in a photo editing extension.

> **Note**:  For design guidance, see Human Interface Guidelines > [Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos).

The [`PHLivePhoto`](./phlivephoto.md) class serves in much the same role for Live Photos as the [`UIImage`](../UIKit/uiimage.md) or [`NSImage`](../AppKit/nsimage.md) class serves for static images. A [`UIImage`](../UIKit/uiimage.md) or [`NSImage`](../AppKit/nsimage.md) object represents not the data file an image is loaded from, but instead a ready-to-use image that can be displayed in a view—similarly, a [`PHLivePhoto`](./phlivephoto.md) object represents a Live Photo ready to display with motion and sound using a [`PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview) object, not an entry in the Photos library or the data resources that constitute a Live Photo. (To work with Live Photos as elements of the Photos library, use the [`PHAsset`](./phasset.md) class. To work with the data files that constitute a Live Photo, use the [`PHAssetResource`](./phassetresource.md) class.)

> 💡 **Tip**:  To display Live Photo content on the web, use the [LivePhotosKit JS](../LivePhotosKitJS/LivePhotosKitJS.md) framework.

## Topics

### Inspecting a Live Photo
- [var size: CGSize](./phlivephoto/size.md)
  The size, in pixels, of the Live Photo.
### Loading a Live Photo from Data Files
- [class func request(withResourceFileURLs: [URL], placeholderImage: UIImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: (PHLivePhoto?, [AnyHashable : Any]) -> Void) -> PHLivePhotoRequestID](./phlivephoto/request%28withresourcefileurls,placeholderimage,targetsize,contentmode,resulthandler%29.md)
  Asynchronously loads a Live Photo from the specified resource files.
- [class func cancelRequest(withRequestID: PHLivePhotoRequestID)](./phlivephoto/cancelrequest%28withrequestid%29.md)
  Cancels an asynchronous request
### Constants
- [typealias PHLivePhotoRequestID](./phlivephotorequestid.md)
  A numeric identifier for an asynchronous Live Photo loading request.
- [Image Request Identifiers](../PhotoKit/image-request-identifiers.md)
  Special values for the Live Photo request ID that are returned by asynchronous requests.
- [Result Handler Info Dictionary Keys](../PhotoKit/result-handler-info-dictionary-keys.md)
  Info describing an attempt to load a Live Photo.
### Initializers
- [init?(coder: NSCoder)](./phlivephoto/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSItemProviderReading](../Foundation/nsitemproviderreading.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transferable](../CoreTransferable/transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephoto)*