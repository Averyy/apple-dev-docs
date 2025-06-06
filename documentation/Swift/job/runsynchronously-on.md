# runSynchronously(on:)

**Framework**: Swift  
**Kind**: method

Run this job on the passed in executor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func runSynchronously(on executor: UnownedSerialExecutor)
```

#### Discussion

This operation runs the job on the calling thread and  until the job completes. The intended use of this method is for an executor to determine when and where it wants to run the job and then call this method on it.

The passed in executor reference is used to establish the executor context for the job, and should be the same executor as the one semantically calling the `runSynchronously` method.

This operation consumes the job, preventing it accidental use after it has been run.

Converting a `ExecutorJob` to an [`UnownedJob`](unownedjob.md) and invoking ``UnownedJob/runSynchronously(_:)` on it multiple times is undefined behavior, as a job can only ever be run once, and must not be accessed after it has been run.

## Parameters

- `executor`: The executor this job will be semantically running on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/job/runsynchronously(on:))*