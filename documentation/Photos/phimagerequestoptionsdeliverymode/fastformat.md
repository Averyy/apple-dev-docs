# PHImageRequestOptionsDeliveryMode.fastFormat

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos provides only a fast-loading image, possibly sacrificing image quality.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case fastFormat
```

```c
PHImageRequestOptionsDeliveryModeFastFormat
```

## Discussion

Photos calls your `resultHandler` block once. If a high-quality image cannot be loaded quickly, the result handler provides a low-quality image. Check the [`PHImageResultIsDegradedKey`](../phimageresultisdegradedkey.md) key in the info dictionary to determine the quality of image provided to the result handler.

This option is available only if the [`isSynchronous`](../phimagerequestoptions/issynchronous.md) property is `false`.

## See Also

### Constants
- [PHImageRequestOptionsDeliveryMode.opportunistic](./opportunistic.md)
  Photos automatically provides one or more results in order to balance image quality and responsiveness.
- [PHImageRequestOptionsDeliveryMode.highQualityFormat](./highqualityformat.md)
  Photos provides only the highest-quality image available, regardless of how much time it takes to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/fastformat)*