# requestLivePhoto(for:targetSize:contentMode:options:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests a Live Photo representation for the specified asset.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestLivePhoto(for asset: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

```objc
- (PHImageRequestID) requestLivePhotoForAsset:(PHAsset *) asset targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode options:(PHLivePhotoRequestOptions *) options resultHandler:(void (^)(PHLivePhoto *livePhoto, NSDictionary *info)) resultHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

#### Discussion

A Live Photo is a picture, taken with a supported device, that includes movement and sound from the moments just before and after its capture. Much like how a [`UIImage`](../../UIKit/uiimage.md) object represents a ready-to-use form of an image, a [`PHLivePhoto`](../phlivephoto.md) object represents a Live Photo whose image, motion, and sound data are prepared for display. Use this method to request an asset’s Live Photo form; after Photos calls your `resultHandler` block to provide the Live Photo, you can display it using the [`PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview) class.

> **Note**:  Use this method only when you plan to display the motion and sound content associated with a Live Photo. In contexts where you need only a still image for a Live Photo asset—for example, when loading thumbnails to display in a photo chooser interface—use the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](./requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method instead.

When you call this method, Photos loads or generates a [`PHLivePhoto`](../phlivephoto.md) object for the asset at, or near, the size you specify. Next, it calls your `resultHandler` block to provide the requested image. To serve your request more quickly, Photos may provide an image that is slightly larger than the target size—either because such an image is already cached or because it can be generated more efficiently. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network. This method always executes asynchronously.

Photos may call your result handler block more than once. Photos first calls the block to provide a low-quality image suitable for displaying temporarily while it prepares a high-quality image. (If low-quality image data is immediately available, the first call may occur before the method returns.) When the high-quality image is ready, Photos calls your result handler again to provide it. If the image manager has already cached the requested image at full quality, Photos calls your result handler only once. The [`PHImageResultIsDegradedKey`](../phimageresultisdegradedkey.md) key in the result handler’s `info` parameter indicates when Photos is providing a temporary low-quality image.

## Parameters

- `asset`: The asset whose Live Photo data is to be loaded.
- `targetSize`: The target size of Live Photo to be returned.
- `contentMode`: An option for how to fit the image to the aspect ratio of the requested size. For details, see [`PHImageContentMode`](../phimagecontentmode.md).
- `options`: Options specifying how Photos should handle the request, format the requested image, and notify your app of progress or errors. For details, see [`PHLivePhotoRequestOptions`](../phlivephotorequestoptions.md).
- `resultHandler`: A block to be called when image loading is complete, providing the requested image or information about the status of the request.

  The block takes the following parameters:

  - **result**: The requested Live Photo object.
  - **info**: A dictionary providing information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestlivephoto(for:targetsize:contentmode:options:resulthandler:))*