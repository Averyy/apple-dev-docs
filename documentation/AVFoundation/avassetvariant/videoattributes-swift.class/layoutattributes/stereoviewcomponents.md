# stereoViewComponents

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

In the case of 3D or stereoscopic content, the value contains [`leftEye`](https://developer.apple.com/documentation/CoreMedia/CMStereoViewComponents/leftEye) and [`rightEye`](https://developer.apple.com/documentation/CoreMedia/CMStereoViewComponents/rightEye) components. In the case of monoscopic content, this value is [`kCMStereoView_None`](https://developer.apple.com/documentation/CoreMedia/CMStereoViewComponents/kCMStereoView_None).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes/stereoviewcomponents)*