# runSynchronously(on:)

**Framework**: Swift  
**Kind**: method

Run this job on the passed in executor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func runSynchronously(on executor: UnownedSerialExecutor)
```

#### Discussion

This operation runs the job on the calling thread and  until the job completes. The intended use of this method is for an executor to determine when and where it wants to run the job and then call this method on it.

The passed in executor reference is used to establish the executor context for the job, and should be the same executor as the one semantically calling the `runSynchronously` method.

## Parameters

- `executor`: The executor this job will be semantically running on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedjob/runsynchronously(on:)-o1nb)*