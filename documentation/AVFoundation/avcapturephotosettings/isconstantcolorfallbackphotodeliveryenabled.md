# isConstantColorFallbackPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isConstantColorFallbackPhotoDeliveryEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isConstantColorFallbackPhotoDeliveryEnabled) BOOL constantColorFallbackPhotoDeliveryEnabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Set the value to [`true`](../../Swift/true.md) to receive a fallback photo that you can use if the main constant color photo’s confidence level doesn’t meet your requirement.

## See Also

### Configuring constant color
- [var isConstantColorEnabled: Bool](./isconstantcolorenabled.md)
  A Boolean value that indicates whether to capture the photo with constant color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled)*