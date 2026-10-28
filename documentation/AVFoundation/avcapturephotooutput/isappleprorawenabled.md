# isAppleProRAWEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isAppleProRAWEnabled) BOOL appleProRAWEnabled;
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](../capturing-photos-in-raw-and-apple-proraw-formats.md)

## Discussion

If [`isAppleProRAWSupported`](./isappleprorawsupported.md) returns [`true`](../../Swift/true.md), you can enable Apple ProRAW capture by setting this property to [`true`](../../Swift/true.md). Compared to photos taken in Bayer RAW format, the system demosaics and partially processes Apple ProRAW photos. They’re still scene-referred, however, and allow capturing RAW photos in modes that don’t have a traditional Bayer RAW format available, such as modes that rely on fusing multiple captures.

Apple ProRAW formats aren’t supported on all platforms and devices. You can determine the pixel formats the system supports by querying the [`availableRawPhotoPixelFormatTypes`](./availablerawphotopixelformattypes-9t9k5.md) property. Use the [`isBayerRAWPixelFormat(_:)`](./isbayerrawpixelformat%28_%29.md) or [`isAppleProRAWPixelFormat(_:)`](./isappleprorawpixelformat%28_%29.md) method to determine whether the pixel format is Bayer RAW or Apple ProRAW, respectively.

This property is key-value observable.

> 💡 **Tip**:  Set this property to [`true`](../../Swift/true.md) before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md) on the capture session. Enabling this property later requires a lengthy reconfiguration of the capture pipeline.

## See Also

### Configuring ProRAW support
- [var isAppleProRAWSupported: Bool](./isappleprorawsupported.md)
  A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawenabled)*