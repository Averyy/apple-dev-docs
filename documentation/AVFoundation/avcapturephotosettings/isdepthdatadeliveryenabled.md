# isDepthDataDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether the photo output captures depth data along with the photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isDepthDataDeliveryEnabled: Bool { get set }
```

#### Discussion

When this property is  [`false`](https://developer.apple.com/documentation/swift/false) (the default), the capture output produces only photo data and metadata.

If you change this property to [`true`](https://developer.apple.com/documentation/swift/true), the capture output records per-pixel scene depth information and delivers an [`AVDepthData`](avdepthdata.md) object in the photo capture results. Enabling depth capture for a photo capture request requires that the photo output first be configured for depth capture using its own [`isDepthDataDeliveryEnabled`](avcapturephotooutput/isdepthdatadeliveryenabled.md) property (and raises an exception otherwise).

> **Note**:  Enabling depth capture along with photo capture adds significant processing time before delivery of results to your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method.

## See Also

- [var embedsDepthDataInPhoto: Bool](avcapturephotosettings/embedsdepthdatainphoto.md)
  A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.
- [var isDepthDataFiltered: Bool](avcapturephotosettings/isdepthdatafiltered.md)
  A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdepthdatadeliveryenabled)*