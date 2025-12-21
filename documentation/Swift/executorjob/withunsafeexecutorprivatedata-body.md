# withUnsafeExecutorPrivateData(body:)

**Framework**: Swift  
**Kind**: method

Execute a closure, passing it the bounds of the executor private data for the job.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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