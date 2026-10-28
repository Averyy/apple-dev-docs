# PHImageRequestOptionsDeliveryMode.highQualityFormat

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos provides only the highest-quality image available, regardless of how much time it takes to load.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case highQualityFormat
```

```c
PHImageRequestOptionsDeliveryModeHighQualityFormat
```

## Discussion

If the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property is `true` or if using the [`requestImageDataForAsset:options:resultHandler:`](../phimagemanager/requestimagedataforasset_options_resulthandler_.md) method, this behavior is the default and only option (that is, specifying other delivery mode options has no effect).

## See Also

### Constants
- [PHImageRequestOptionsDeliveryMode.opportunistic](./opportunistic.md)
  Photos automatically provides one or more results in order to balance image quality and responsiveness.
- [PHImageRequestOptionsDeliveryMode.fastFormat](./fastformat.md)
  Photos provides only a fast-loading image, possibly sacrificing image quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/highqualityformat)*