# embedsPortraitEffectsMatteInPhoto

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Specifies whether the portrait effects matte captured with ths photo should be written to the photo’s file structure.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var embedsPortraitEffectsMatteInPhoto: Bool { get set }
```

```objc
@property (nonatomic) BOOL embedsPortraitEffectsMatteInPhoto;
```

## Discussion

The default is [`true`](../../Swift/true.md), which tells AV Foundation to embed the portrait effects matte images as HEIF and JPEG in the photo.

This property is ignored if [`isPortraitEffectsMatteDeliveryEnabled`](./isportraiteffectsmattedeliveryenabled.md) is set to [`false`](../../Swift/false.md). AV Foundation includes the portrait effects matte only if both this property and [`isPortraitEffectsMatteDeliveryEnabled`](./isportraiteffectsmattedeliveryenabled.md) are set to [`true`](../../Swift/true.md).

## See Also

### Capturing Portrait Effects matte
- [var isPortraitEffectsMatteDeliveryEnabled: Bool](./isportraiteffectsmattedeliveryenabled.md)
  Specifies whether a portrait effects matte should be captured along with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedsportraiteffectsmatteinphoto)*