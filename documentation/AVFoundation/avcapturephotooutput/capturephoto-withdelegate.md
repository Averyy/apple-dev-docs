# capturePhoto(with:delegate:)

**Framework**: AVFoundation  
**Kind**: method

Initiates a photo capture using the specified settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func capturePhoto(with settings: AVCapturePhotoSettings, delegate: any AVCapturePhotoCaptureDelegate)
```

## Mentions

- [Capturing a bracketed photo sequence](capturing-a-bracketed-photo-sequence.md)
- [Capturing and saving Live Photos](capturing-and-saving-live-photos.md)
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
- [Capturing photos with depth](capturing-photos-with-depth.md)
- [Setting up a capture session](setting-up-a-capture-session.md)
- [Tracking photo capture progress](tracking-photo-capture-progress.md)

#### Discussion

Use this method for all variations of still photography, including single photo capture,  RAW format capture (with or without a secondary format such as JPEG), bracketed capture of multiple images, and Live Photo capture.

When you call this method, the photo output validates the properties of your `settings` object to ensure deterministic behavior. For example, the [`flashMode`](avcapturephotosettings/flashmode.md) setting must specify a value that is present in the photo output’s [`supportedFlashModes`](avcapturephotooutput/supportedflashmodes-4u69s.md) array. See each property’s description in the [`AVCapturePhotoSettings`](avcapturephotosettings.md) class reference for detailed validation rules.

## Parameters

- `settings`: The settings for the photo capture, such as the output pixel format and flash mode. This method copies the provided   object, so future changes to that object do not affect the capture in progress.
- `delegate`: A delegate object to receive messages about capture progress and results. The photo output calls your delegate methods as the photo advances from capture to processing to delivery of finished images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturephoto(with:delegate:))*