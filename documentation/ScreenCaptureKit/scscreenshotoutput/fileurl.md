# fileURL

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A URL property that specifies the location of the saved image.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
unowned(unsafe) var fileURL: NSURL? { get set }
```

```objc
@property (nonatomic, assign, nullable) NSURL * fileURL;
```

## Discussion

If `fileURL` is `nil`, then the file isn’t saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotoutput/fileurl)*