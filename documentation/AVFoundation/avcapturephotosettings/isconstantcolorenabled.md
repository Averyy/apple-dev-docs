# isConstantColorEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isConstantColorEnabled) BOOL constantColorEnabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Set the value to [`true`](../../Swift/true.md) to capture a constant color photo.

> ❗ **Important**:  Attempting to enable constant color capture when a photo output’s [`isConstantColorEnabled`](../avcapturephotooutput/isconstantcolorenabled.md) is [`false`](../../Swift/false.md), results in the system throwing an exception.

## See Also

### Configuring constant color
- [var isConstantColorFallbackPhotoDeliveryEnabled: Bool](./isconstantcolorfallbackphotodeliveryenabled.md)
  A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorenabled)*