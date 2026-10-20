# timestamp

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time at which the image was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var timestamp: CMTime { get }
```

```objc
@property (readonly) CMTime timestamp;
```

#### Discussion

This timestamp is always synchronized to the [`masterClock`](../avcapturesession/masterclock.md) time of the [`AVCaptureSession`](../avcapturesession.md) object to which the photo output is connected.

## See Also

### Resolving photo capture requests
- [var resolvedSettings: AVCaptureResolvedPhotoSettings](./resolvedsettings.md)
  The settings object that was used to request this photo capture.
- [var photoCount: Int](./photocount.md)
  The 1-based index of this photo capture relative to other results from the same capture request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/timestamp)*