# isConstantColorFallbackPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to receive a fallback photo that you can use if the main constant color photo’s confidence level doesn’t meet your requirement.

## See Also

- [var isConstantColorEnabled: Bool](avcapturephotosettings/isconstantcolorenabled.md)
  A Boolean value that indicates whether to capture the photo with constant color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled)*