# isPortraitEffectsMatteDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

Specifies whether a portrait effects matte should be captured along with the photo.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isPortraitEffectsMatteDeliveryEnabled: Bool { get set }
```

#### Discussion

The default is `NO`.  Set to `YES` if you wish to receive a portrait effects matte with your photo. AVFoundation throws an exception if [`isPortraitEffectsMatteDeliveryEnabled`](avcapturephotooutput/isportraiteffectsmattedeliveryenabled.md) is not set to `YES`, or if your delegate doesn’t respond to the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) selector.

> ❗ **Important**:  Portrait effects matte generation requires depth data to be present, so you must also set [`isDepthDataDeliveryEnabled`](avcapturephotooutput/isdepthdatadeliveryenabled.md) to `YES`.

Setting this property to `YES` doen’t guarantee that a portrait effects matte will be present in the resulting [`AVCapturePhoto`](avcapturephoto.md). The matte is primarily used to improve the rendering quality of portrait effects on the image. If the photo’s content lacks a clear foreground subject, no portrait effects matte is generated, and the property returns `nil`. Setting this property to `YES` may add significant processing time to the delivery of your [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) callback.

## See Also

- [var embedsPortraitEffectsMatteInPhoto: Bool](avcapturephotosettings/embedsportraiteffectsmatteinphoto.md)
  Specifies whether the portrait effects matte captured with ths photo should be written to the photo’s file structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isportraiteffectsmattedeliveryenabled)*