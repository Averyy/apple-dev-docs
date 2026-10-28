# PHImageRequestOptionsDeliveryMode.opportunistic

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos automatically provides one or more results in order to balance image quality and responsiveness.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case opportunistic
```

```c
PHImageRequestOptionsDeliveryModeOpportunistic
```

## Discussion

If the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property is `false`, Photos may call the `resultHandler` block (that you specified in the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](../phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method more than once. Photos may call your result handler once to provide a low-quality image suitable for displaying temporarily while it prepares a high-quality image. If low-quality image data is immediately available, this first call may occur before the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](../phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method returns. When the high-quality image is ready, Photos calls your result handler again to provide it.

If the image manager has already cached the requested image, or if the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property is `true`, Photos calls your result handler only once.

## See Also

### Constants
- [PHImageRequestOptionsDeliveryMode.highQualityFormat](./highqualityformat.md)
  Photos provides only the highest-quality image available, regardless of how much time it takes to load.
- [PHImageRequestOptionsDeliveryMode.fastFormat](./fastformat.md)
  Photos provides only a fast-loading image, possibly sacrificing image quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/opportunistic)*