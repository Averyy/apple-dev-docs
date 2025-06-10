# withUnsafeExecutorPrivateData(body:)

**Framework**: Swift  
**Kind**: method

Execute a closure, passing it the bounds of the executor private data for the job.

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
func withUnsafeExecutorPrivateData<R, E>(body: (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R where E : Error
```

#### Discussion

Parameters:

- body: The closure to execute.

Returns the result of executing the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/withunsafeexecutorprivatedata(body:))*