# stopCapture()

**Framework**: Metal  
**Kind**: method

Stops capturing Metal commands.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func stopCapture()
```

#### Discussion

Calling this method stops a capture that was started manually in Xcode or programmatically by calling one of the methods on [`MTLCaptureManager`](mtlcapturemanager.md).

When using a custom capture scope, calling this function preempts any [`end()`](mtlcapturescope/end().md) demarcations of the capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturemanager/stopcapture())*