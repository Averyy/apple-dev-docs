# stereoViewComponents

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Attributes that describe the video’s stereo components.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var stereoViewComponents: CMStereoViewComponents { get }
```

```objc
@property (nonatomic, readonly) CMStereoViewComponents stereoViewComponents;
```

## Discussion

In the case of 3D or stereoscopic content, the value contains [`leftEye`](../../../../CoreMedia/cmstereoviewcomponents/lefteye.md) and [`rightEye`](../../../../CoreMedia/cmstereoviewcomponents/righteye.md) components. In the case of monoscopic content, this value is [`kCMStereoView_None`](../../../../CoreMedia/cmstereoviewcomponents/kcmstereoview_none.md).

## See Also

### Accessing attributes
- [var projectionType: CMProjectionType](./projectiontype.md)
  Describes the video projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes/stereoviewcomponents)*