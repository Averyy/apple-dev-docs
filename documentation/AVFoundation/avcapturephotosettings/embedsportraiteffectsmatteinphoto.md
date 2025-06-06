# embedsPortraitEffectsMatteInPhoto

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The default is [`true`](https://developer.apple.com/documentation/swift/true), which tells AV Foundation to embed the portrait effects matte images as HEIF and JPEG in the photo.

This property is ignored if [`isPortraitEffectsMatteDeliveryEnabled`](avcapturephotosettings/isportraiteffectsmattedeliveryenabled.md) is set to [`false`](https://developer.apple.com/documentation/swift/false). AV Foundation includes the portrait effects matte only if both this property and [`isPortraitEffectsMatteDeliveryEnabled`](avcapturephotosettings/isportraiteffectsmattedeliveryenabled.md) are set to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var isPortraitEffectsMatteDeliveryEnabled: Bool](avcapturephotosettings/isportraiteffectsmattedeliveryenabled.md)
  Specifies whether a portrait effects matte should be captured along with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedsportraiteffectsmatteinphoto)*