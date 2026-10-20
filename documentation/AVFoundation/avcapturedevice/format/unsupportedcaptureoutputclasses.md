# unsupportedCaptureOutputClasses

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The list of capture output subclasses not allowed for capture with this format, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var unsupportedCaptureOutputClasses: [AnyClass] { get }
```

```objc
@property (nonatomic, readonly) NSArray<Class> * unsupportedCaptureOutputClasses;
```

#### Discussion

As a rule, capture formats with a given [`mediaType`](./mediatype.md) are available for use with all [`AVCaptureOutput`](../../avcaptureoutput.md) subclasses that accept that media type. However, this isn’t always the case. For example, formats for high-resolution photo capture may not support the [`AVCaptureMovieFileOutput`](../../avcapturemoviefileoutput.md) class due to bandwidth limitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/unsupportedcaptureoutputclasses)*