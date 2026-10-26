# requestImage(for:targetSize:contentMode:options:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests an image representation for the specified asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func requestImage(for asset: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: @escaping (UIImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

*macOS*

```swift
func requestImage(for asset: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: @escaping (NSImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PHImageRequestID) requestImageForAsset:(PHAsset *) asset targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode options:(PHImageRequestOptions *) options resultHandler:(void (^)(UIImage *result, NSDictionary *info)) resultHandler;
```

*macOS*

```objc
- (PHImageRequestID) requestImageForAsset:(PHAsset *) asset targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode options:(PHImageRequestOptions *) options resultHandler:(void (^)(NSImage *result, NSDictionary *info)) resultHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

#### Discussion

When you call this method, Photos loads or generates an image of the asset at, or near, the size you specify. Next, it calls your `resultHandler` block to provide the requested image. To serve your request more quickly, Photos may provide an image that is slightly larger than the target size—either because such an image is already cached or because it can be generated more efficiently. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

By default, this method executes asynchronously. If you call it from a background thread you may change the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property of the `options` parameter to `true` to block the calling thread until either the requested image is ready or an error occurs, at which time Photos calls your result handler.

For an asynchronous request, Photos may call your result handler block more than once. Photos first calls the block to provide a low-quality image suitable for displaying temporarily while it prepares a high-quality image. (If low-quality image data is immediately available, the first call may occur before the method returns.) When the high-quality image is ready, Photos calls your result handler again to provide it. If the image manager has already cached the requested image at full quality, Photos calls your result handler only once. The [`PHImageResultIsDegradedKey`](../phimageresultisdegradedkey.md) key in the result handler’s `info` parameter indicates when Photos is providing a temporary low-quality image.

You can use this method for both photo and video assets—for a video asset, an image request provides a thumbnail image or poster frame.

## Parameters

- `asset`: The asset whose image data is to be loaded.
- `targetSize`: The target size of image to be returned.
- `contentMode`: An option for how to fit the image to the aspect ratio of the requested size. For details, see [`PHImageContentMode`](../phimagecontentmode.md).
- `options`: Options specifying how Photos should handle the request, format the requested image, and notify your app of progress or errors. For details, see [`PHImageRequestOptions`](../phimagerequestoptions.md).
- `resultHandler`: A block to be called when image loading is complete, providing the requested image or information about the status of the request.

  The block takes the following parameters:

  - **result**: The requested image.
  - **info**: A dictionary providing information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.

## See Also

### Requesting Images
- [func requestImageDataAndOrientation(for: PHAsset, options: PHImageRequestOptions?, resultHandler: (Data?, String?, CGImagePropertyOrientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestimagedataandorientation%28for,options,resulthandler%29.md)
  Requests the largest represented image as data bytes and Exif orientation for the specified asset.
- [let PHImageManagerMaximumSize: CGSize](../phimagemanagermaximumsize.md)
  A special value for requesting original image data or the largest rendered image available. .
- [- requestImageDataForAsset:options:resultHandler:](./requestimagedataforasset_options_resulthandler_.md)
  Requests full-sized image data for the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestimage(for:targetsize:contentmode:options:resulthandler:))*