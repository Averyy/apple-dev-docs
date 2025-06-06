# error

**Framework**: AVFoundation  
**Kind**: property

An error that describes the reason looping failed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The value of this property is `nil` unless the looper’s [`status`](avplayerlooper/status-swift.property.md) changes to [`AVPlayerLooper.Status.failed`](avplayerlooper/status-swift.enum/failed.md). If this occurs, this property value contains an error object that provides the details of the error that prevented looping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/error)*