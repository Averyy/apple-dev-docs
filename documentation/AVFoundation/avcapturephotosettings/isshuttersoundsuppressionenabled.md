# isShutterSoundSuppressionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to suppress the built-in shutter sound when capturing a photo.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isShutterSoundSuppressionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isShutterSoundSuppressionEnabled) BOOL shutterSoundSuppressionEnabled;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). Set the value to [`true`](../../Swift/true.md) to suppress the photo output’s built-in shutter sound for this request. The photo output throws an invalid argument exception when calling [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) if its [`isShutterSoundSuppressionSupported`](../avcapturephotooutput/isshuttersoundsuppressionsupported.md) property returns [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isshuttersoundsuppressionenabled)*