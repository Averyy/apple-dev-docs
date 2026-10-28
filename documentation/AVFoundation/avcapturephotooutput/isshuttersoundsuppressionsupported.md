# isShutterSoundSuppressionSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the photo output supports suppressing the system shutter sound.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isShutterSoundSuppressionSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isShutterSoundSuppressionSupported) BOOL shutterSoundSuppressionSupported;
```

## Discussion

In iOS, the value is [`true`](../../Swift/true.md), except in jurisdictions where you can’t disable the shutter sound. On all other platforms, the value is always [`false`](../../Swift/false.md).

If the output supports this feature, you can supress the shutter sound when capturing a photo using the [`isShutterSoundSuppressionEnabled`](../avcapturephotosettings/isshuttersoundsuppressionenabled.md) property of [`AVCapturePhotoSettings`](../avcapturephotosettings.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isshuttersoundsuppressionsupported)*