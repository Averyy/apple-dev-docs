# isConstantColorEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether to capture the photo with constant color.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isConstantColorEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). Set the value to [`true`](https://developer.apple.com/documentation/swift/true) to capture a constant color photo.

> ❗ **Important**:  Attempting to enable constant color capture when a photo output’s [`isConstantColorEnabled`](avcapturephotooutput/isconstantcolorenabled.md) is [`false`](https://developer.apple.com/documentation/swift/false), results in the system throwing an exception.

 Attempting to enable constant color capture when a photo output’s [`isConstantColorEnabled`](avcapturephotooutput/isconstantcolorenabled.md) is [`false`](https://developer.apple.com/documentation/swift/false), results in the system throwing an exception.

## See Also

- [var isConstantColorFallbackPhotoDeliveryEnabled: Bool](avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled.md)
  A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorenabled)*