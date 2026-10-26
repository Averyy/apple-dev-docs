# request(withResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Asynchronously loads a Live Photo from the specified resource files.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
class func request(withResourceFileURLs fileURLs: [URL], placeholderImage image: UIImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]) -> Void) -> PHLivePhotoRequestID
```

*macOS*

```swift
class func request(withResourceFileURLs fileURLs: [URL], placeholderImage image: NSImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]) -> Void) -> PHLivePhotoRequestID
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
+ (PHLivePhotoRequestID) requestLivePhotoWithResourceFileURLs:(NSArray<NSURL *> *) fileURLs placeholderImage:(UIImage *) image targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode resultHandler:(void (^)(PHLivePhoto *livePhoto, NSDictionary *info)) resultHandler;
```

*macOS*

```objc
+ (PHLivePhotoRequestID) requestLivePhotoWithResourceFileURLs:(NSArray<NSURL *> *) fileURLs placeholderImage:(NSImage *) image targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode resultHandler:(void (^)(PHLivePhoto *livePhoto, NSDictionary *info)) resultHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelRequest(withRequestID:)`](./cancelrequest%28withrequestid%29.md) method.

#### Discussion

Use this method to load Live Photo objects for display from data files previously exported from a Photos library. For example, a social networking app can use the [`PHAssetResource`](../phassetresource.md) class to retrieve the data files that constitute a Live Photo in one user’s library and upload them to a server. Then, on another user’s device, the app downloads those data files and uses this method to re-create a Live Photo object for display using the [`PHLivePhotoView`](../../PhotosUI/phlivephotoview.md) class.

> **Note**:  To instead obtain a [`PHLivePhoto`](../phlivephoto.md) object representing a Live Photo asset from the user’s Photos library, use the [`PHAsset`](../phasset.md) class to locate the asset and the [`PHImageManager`](../phimagemanager.md) class to fetch the asset’s Live Photo data for display.
>
> To instead import a Live Photo to the Photos library, use the [`PHAssetCreationRequest`](../phassetcreationrequest.md) class.

This method is asynchronous. Photos loads, validates, and prepares data on a background thread, then calls your `resultHandler` block with a ready-to-display Live Photo object. Like the similar methods in the PHImageManager class, Photos can call your result handler block more than once—first, to provide a low-quality Live Photo object (consisting of only the static image from the `image` parameter), then later to provide the full motion and sound content of the Live Photo. If the [`PHLivePhotoInfoIsDegradedKey`](../phlivephotoinfoisdegradedkey.md) value in your result handler’s `info` dictionary is `true`, Photos will call your result handler again.

This method can load a [`PHLivePhoto`](../phlivephoto.md) object only from the same set of files exported from a previously captured Live Photo asset. When you use this method, Photos validates that the files and their metadata can be loaded as a Live Photo. If Photos cannot load a Live Photo from the specified files, the `result` parameter in your result handler block is `nil`, and the `info` dictionary contains an `NSError` object describing the error.

## Parameters

- `fileURLs`: An array of URLs containing only the still URL and the video URL that constitute a Live Photo, as obtained using the [`PHAssetResource`](../phassetresource.md) class.
- `image`: A static image to represent the Live Photo before its full content has been loaded and validated.
- `targetSize`: The target size of Live Photo to be returned. Pass `CGSizeZero` to obtain the requested Live Photo at its original size.
- `contentMode`: An option for how to fit the image to the aspect ratio of the requested size. For details, see [`PHLivePhoto`](../phlivephoto.md).
- `resultHandler`: A block to be called when image loading is complete, providing the requested Live Photo or information about the status of the request.

  The block takes the following parameters:

  - **result**: The requested Live Photo object.
  - **info**: A dictionary providing information about the status of the request. See [`PHLivePhoto`](../phlivephoto.md) for possible keys and values.

## See Also

### Loading a Live Photo from Data Files
- [class func cancelRequest(withRequestID: PHLivePhotoRequestID)](./cancelrequest%28withrequestid%29.md)
  Cancels an asynchronous request


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephoto/request(withresourcefileurls:placeholderimage:targetsize:contentmode:resulthandler:))*