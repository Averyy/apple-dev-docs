# shared()

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Type Method

Returns an app’s instance of the shared screen recorder.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit instead

## Declaration

```swift
class func shared() -> RPScreenRecorder
```

```objc
+ (RPScreenRecorder *) sharedRecorder;
```

## Return Value

An `RPScreenRecorder` object.

## Discussion

Use [`shared()`](./shared%28%29.md) to access the shared recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/shared())*