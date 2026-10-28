# supportedContentTypes

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Type Property

An array of uniform type identifiers that correspond to file formats the output image supports.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class var supportedContentTypes: [UTType] { get }
```

```objc
@property (class, readonly) NSArray<UTType *> * supportedContentTypes;
```

## Discussion

You can save the output [`CGImage`](../../CoreGraphics/cgimage.md) into HEIC, JPEG, and PNG formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/supportedcontenttypes)*