# supportedContentTypes

**Framework**: ScreenCaptureKit  
**Kind**: property

An array of uniform type identifiers that correspond to file formats the output image supports.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class var supportedContentTypes: [UTType] { get }
```

#### Discussion

You can save the output [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) into HEIC, JPEG, and PNG formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/supportedcontenttypes)*