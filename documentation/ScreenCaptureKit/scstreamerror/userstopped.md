# userStopped

**Framework**: ScreenCaptureKit  
**Kind**: property

An error message that indicates the user stopped the stream.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var userStopped: SCStreamError.Code { get }
```

#### Discussion

As a best practice, handle errors of this type as an intentional user interaction rather than an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/userstopped)*