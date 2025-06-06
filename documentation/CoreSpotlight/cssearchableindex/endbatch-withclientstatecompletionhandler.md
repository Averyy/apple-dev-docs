# endBatch(withClientState:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Ends a batch of index updates and stores the specified state information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func endBatch(withClientState clientState: Data) async throws
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

- `clientState`: Up to 250 bytes of information that can help you recover from a crash and resume indexing.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func beginBatch()](cssearchableindex/beginbatch.md)
  Begins a batch of updates to an index.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func fetchLastClientState(completionHandler: (Data?, (any Error)?) -> Void)](cssearchableindex/fetchlastclientstate(completionhandler:).md)
  Fetches the app’s most recent client state information asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/endbatch(withclientstate:completionhandler:))*