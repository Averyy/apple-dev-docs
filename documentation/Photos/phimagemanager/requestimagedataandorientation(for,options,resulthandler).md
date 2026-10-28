# requestImageDataAndOrientation(for:options:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests the largest represented image as data bytes and Exif orientation for the specified asset.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func requestImageDataAndOrientation(for asset: PHAsset, options: PHImageRequestOptions?, resultHandler: @escaping (Data?, String?, CGImagePropertyOrientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

```objc
- (PHImageRequestID) requestImageDataAndOrientationForAsset:(PHAsset *) asset options:(PHImageRequestOptions *) options resultHandler:(void (^)(NSData *imageData, NSString *dataUTI, CGImagePropertyOrientation orientation, NSDictionary *info)) resultHandler;
```

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

## Discussion

When you call this method, Photos loads the largest available representation of the image asset, then calls your `resultHandler` block to provide the requested data. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

By default, this method executes asynchronously. If you call it from a background thread, you may change the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property of the `options` parameter to `true` to block the calling thread until either the requested image is ready or an error occurs, at which time Photos calls your result handler. This method ignores the [`deliveryMode`](../phimagerequestoptions/deliverymode.md) option—Photos calls your result handler block exactly once.

If the [`version`](../phimagerequestoptions/version.md) option is set to [`PHImageRequestOptionsVersion.current`](../phimagerequestoptionsversion/current.md), Photos provides rendered image data, including the results of any edits that have been made to the asset content. Otherwise, Photos provides the originally captured image data for the asset.

## Parameters

- `asset`: The asset for which to load image data.
- `options`: Options specifying how Photos should handle the request, format the requested image, and notify your app of progress or errors.

  If [`PHImageRequestOptionsVersion.current`](../phimagerequestoptionsversion/current.md) is requested and the asset has adjustments, the largest rendered image data is returned. In all other cases, the original image data is returned.

  For further details, see [`PHImageRequestOptions`](../phimagerequestoptions.md).
- `resultHandler`: A block called, exactly once, when image loading is complete, providing the requested image or information about the status of the request.

  The block takes the following parameters:

  - **imageData**: The requested image.
  - **dataUTI**: The uniform type identifier for the image.
  - **orientation**: The Exif orientation for the image, as a [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md). For iOS or tvOS, convert this orientation to a [`UIImage.Orientation`](../../UIKit/uiimage/orientation.md).
  - **info**: A dictionary providing information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.

## See Also

### Requesting Images
- [func requestImage(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestimage%28for,targetsize,contentmode,options,resulthandler%29.md)
  Requests an image representation for the specified asset.
- [let PHImageManagerMaximumSize: CGSize](../phimagemanagermaximumsize.md)
  A special value for requesting original image data or the largest rendered image available. .
- [- requestImageDataForAsset:options:resultHandler:](./requestimagedataforasset_options_resulthandler_.md)
  Requests full-sized image data for the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestimagedataandorientation(for:options:resulthandler:))*