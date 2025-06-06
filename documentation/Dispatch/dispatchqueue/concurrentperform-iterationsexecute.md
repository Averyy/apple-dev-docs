# concurrentPerform(iterations:execute:)

**Framework**: Dispatch  
**Kind**: method

Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@preconcurrency
class func concurrentPerform(iterations: Int, execute work: (Int) -> Void)
```

#### Discussion

This method implements an efficient parallel for-loop. The dispatch queue executes the submitted block the specified number of times and waits for all iterations to complete before returning. If the target queue is a concurrent queue, the blocks run in parallel and must therefore be reentrant-safe.

## Parameters

- `iterations`: The number of times to execute the block. Higher iteration values give the system the ability to balance more efficiently across multiple cores. To get the maximum benefit of this function, configure the number of iterations to be at least three times the number of available cores.
- `work`: The block to execute in parallel. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/concurrentperform(iterations:execute:))*