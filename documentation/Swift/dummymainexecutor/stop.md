# stop()

**Framework**: Swift  
**Kind**: method

Signal to the run loop to stop running and return.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func stop()
```

#### Discussion

This method may be called from the same thread that is in the `run()` method, or from some other thread.  It will not wait for the run loop to stop; calling this method simply signals that the run loop , as soon as is practicable, stop the innermost `run()` invocation and make that `run()` invocation return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummymainexecutor/stop())*