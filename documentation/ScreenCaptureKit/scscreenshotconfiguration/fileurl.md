# fileURL

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

Specifies the URL where the screenshot process saves the output.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var fileURL: URL? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSURL * fileURL;
```

## Discussion

If `imageOutputURL` is `nil`, then the file isn’t saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/fileurl)*