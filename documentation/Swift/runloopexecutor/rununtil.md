# runUntil(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Run the executor’s run loop until a condition is satisfied.

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
func runUntil(_ condition: () -> Bool) throws
```

#### Discussion

Not every `RunLoopExecutor` will support this method; you must not call it unless you  that it is supported.  The default implementation generates a fatal error.

Parameters:

- condition: A closure that returns `true` if the run loop should stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/runloopexecutor/rununtil(_:))*