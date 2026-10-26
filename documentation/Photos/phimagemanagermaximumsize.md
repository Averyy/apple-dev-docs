# PHImageManagerMaximumSize

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A special value for requesting original image data or the largest rendered image available. .

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHImageManagerMaximumSize: CGSize
```

```c
extern const CGSize PHImageManagerMaximumSize;
```

#### Discussion

When you use the [`PHImageManagerMaximumSize`](./phimagemanagermaximumsize.md) option, Photos provides the largest image available for the asset without scaling or cropping. (That is, it ignores the [`resizeMode`](./phimagerequestoptions/resizemode.md) option.)

## See Also

### Requesting Images
- [func requestImage(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md)
  Requests an image representation for the specified asset.
- [func requestImageDataAndOrientation(for: PHAsset, options: PHImageRequestOptions?, resultHandler: (Data?, String?, CGImagePropertyOrientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestimagedataandorientation%28for,options,resulthandler%29.md)
  Requests the largest represented image as data bytes and Exif orientation for the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanagermaximumsize)*