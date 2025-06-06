# isLensStabilizationEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLensStabilizationEnabled: Bool { get set }
```

## Mentions

- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Discussion

When this setting is [`true`](https://developer.apple.com/documentation/swift/true), the photo output uses optical image stabilization to hold the lens steady for the duration of the bracketed capture, helping to counter hand shake and produce a sharper bracket of images. The default setting is [`false`](https://developer.apple.com/documentation/swift/false).

You can enable this setting only if the photo output’s [`isLensStabilizationDuringBracketedCaptureSupported`](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md) property is [`true`](https://developer.apple.com/documentation/swift/true). The capture output validates this requirement when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate do not meet this requirement, that method raises an exception.

## See Also

- [var bracketedSettings: [AVCaptureBracketedStillImageSettings]](avcapturephotobracketsettings/bracketedsettings.md)
  An array describing the number of and settings for images to produce in a bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/islensstabilizationenabled)*