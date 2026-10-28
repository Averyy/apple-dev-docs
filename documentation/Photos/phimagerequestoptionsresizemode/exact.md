# PHImageRequestOptionsResizeMode.exact

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Photos resizes the image to match the target size exactly.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case exact
```

```c
PHImageRequestOptionsResizeModeExact
```

## Discussion

Resizing to exactly match a target size is less efficient than using the fast resizing option. The system doesn’t resize low-quality or degraded images that [`PHImageRequestOptionsDeliveryMode.opportunistic`](../phimagerequestoptionsdeliverymode/opportunistic.md) or [`PHImageRequestOptionsDeliveryMode.highQualityFormat`](../phimagerequestoptionsdeliverymode/highqualityformat.md) return.

You must choose this enumeration case if you use the [`normalizedCropRect`](../phimagerequestoptions/normalizedcroprect.md) property to request a cropped image.

## See Also

### Constants
- [PHImageRequestOptionsResizeMode.none](./none.md)
  Photos does not resize the image asset.
- [PHImageRequestOptionsResizeMode.fast](./fast.md)
  Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode/exact)*