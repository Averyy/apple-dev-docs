# fetchLastClientState(completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Fetches the app’s most recent client state information asynchronously.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func fetchLastClientState(completionHandler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func fetchLastClientState() async throws -> Data
```

```objc
- (void) fetchLastClientStateWithCompletionHandler:(void (^)(NSData *clientState, NSError *error)) completionHandler;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func fetchLastClientState() async throws -> Data
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: The block to call when the request has been *journaled* by the index, which means that the index makes a note that it has to perform this operation. Note that the request may not have completed.

  The block receives the following parameter:

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Batching index updates
- [func beginBatch()](./beginbatch%28%29.md)
  Begins a batch of updates to an index.
- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](./endbatch%28withclientstate,completionhandler%29.md)
  Ends a batch of index updates and stores the specified state information.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](./endindexbatch%28expectedclientstate,newclientstate,completionhandler%29.md)
  Ends a batch of index updates and stores the specified state information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/fetchlastclientstate(completionhandler:))*