# embedsDepthDataInPhoto

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var embedsDepthDataInPhoto: Bool { get set }
```

```objc
@property (nonatomic) BOOL embedsDepthDataInPhoto;
```

## Mentions

- [Capturing photos with depth](../capturing-photos-with-depth.md)

## Discussion

When this property is [`true`](../../Swift/true.md) (the default), and depth data capture is enabled with the [`isDepthDataDeliveryEnabled`](./isdepthdatadeliveryenabled.md) property, the [`AVCapturePhoto`](../avcapturephoto.md) class includes the depth map as an embedded attachment when you flatten the photo data for output in compatible file formats.

Set this property to [`false`](../../Swift/false.md) if you wish to capture depth data with a photo but not include depth data in  output.

## See Also

### Capturing depth data
- [var isDepthDataDeliveryEnabled: Bool](./isdepthdatadeliveryenabled.md)
  A Boolean value that determines whether the photo output captures depth data along with the photo.
- [var isDepthDataFiltered: Bool](./isdepthdatafiltered.md)
  A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedsdepthdatainphoto)*