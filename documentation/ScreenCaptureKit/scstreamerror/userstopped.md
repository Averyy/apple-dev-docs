# userStopped

**Framework**: ScreenCaptureKit  
**Kind**: property

An error message that indicates the user stopped the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static var userStopped: SCStreamError.Code { get }
```

#### Discussion

As a best practice, handle errors of this type as an intentional user interaction rather than an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/userstopped)*