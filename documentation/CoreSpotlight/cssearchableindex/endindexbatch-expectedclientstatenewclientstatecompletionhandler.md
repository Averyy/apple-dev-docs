# endIndexBatch(expectedClientState:newClientState:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Ends a batch of index updates and stores the specified state information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func endIndexBatch(expectedClientState: Data?, newClientState: Data) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func endBatch(withClientState clientState: Data) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func endBatch(withClientState clientState: Data) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `expectedClientState`: The client state data from the previous batch.
- `newClientState`: Up to 250 bytes of app-specific data that can help you recover from a crash and resume indexing.
- `completionHandler`: The block to call with the results. The block receives the following parameter:

## See Also

- [func beginBatch()](cssearchableindex/beginbatch.md)
  Begins a batch of updates to an index.
- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endbatch(withclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func fetchLastClientState(completionHandler: (Data?, (any Error)?) -> Void)](cssearchableindex/fetchlastclientstate(completionhandler:).md)
  Fetches the app’s most recent client state information asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:))*