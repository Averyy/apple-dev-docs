# fetchLastClientState(completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Fetches the app’s most recent client state information asynchronously.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func fetchLastClientState() async throws -> Data
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func fetchLastClientState() async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func fetchLastClientState() async throws -> Data
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The block receives the following parameter:

## See Also

- [func beginBatch()](cssearchableindex/beginbatch.md)
  Begins a batch of updates to an index.
- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endbatch(withclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/fetchlastclientstate(completionhandler:))*