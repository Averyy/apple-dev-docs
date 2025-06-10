# run()

**Framework**: Swift  
**Kind**: method

Run the executor’s run loop.

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
final func run() throws
```

#### Discussion

This method will synchronously block the calling thread.  Nested calls to `run()` may be permitted, however it is not permitted to call `run()` on a single executor instance from more than one thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummymainexecutor/run())*