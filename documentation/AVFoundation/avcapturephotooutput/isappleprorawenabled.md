# isAppleProRAWEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether you’ve configured the photo output to deliver Apple ProRAW formats.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- tvOS 17.0+

## Declaration

```swift
var isAppleProRAWEnabled: Bool { get set }
```

## Mentions

- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)

#### Discussion

If [`isAppleProRAWSupported`](avcapturephotooutput/isappleprorawsupported.md) returns [`true`](https://developer.apple.com/documentation/swift/true), you can enable Apple ProRAW capture by setting this property to [`true`](https://developer.apple.com/documentation/swift/true). Compared to photos taken in Bayer RAW format, the system demosaics and partially processes Apple ProRAW photos. They’re still scene-referred, however, and allow capturing RAW photos in modes that don’t have a traditional Bayer RAW format available, such as modes that rely on fusing multiple captures.

Apple ProRAW formats aren’t supported on all platforms and devices. You can determine the pixel formats the system supports by querying the [`availableRawPhotoPixelFormatTypes`](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md) property. Use the [`isBayerRAWPixelFormat(_:)`](avcapturephotooutput/isbayerrawpixelformat(_:).md) or [`isAppleProRAWPixelFormat(_:)`](avcapturephotooutput/isappleprorawpixelformat(_:).md) method to determine whether the pixel format is Bayer RAW or Apple ProRAW, respectively.

This property is key-value observable.

> 💡 **Tip**:  Set this property to [`true`](https://developer.apple.com/documentation/swift/true) before calling [`startRunning()`](avcapturesession/startrunning().md) on the capture session. Enabling this property later requires a lengthy reconfiguration of the capture pipeline.

## See Also

- [var isAppleProRAWSupported: Bool](avcapturephotooutput/isappleprorawsupported.md)
  A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawenabled)*