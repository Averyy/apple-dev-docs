# beginBatch()

**Framework**: Core Spotlight  
**Kind**: method

Begins a batch of updates to an index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func beginBatch()
```

#### Discussion

Don’t call this method again before [`endBatch(withClientState:completionHandler:)`](cssearchableindex/endbatch(withclientstate:completionhandler:).md) has returned. (You can call it again before the completion handler passed to [`endBatch(withClientState:completionHandler:)`](cssearchableindex/endbatch(withclientstate:completionhandler:).md) has been called.)

## See Also

- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endbatch(withclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func fetchLastClientState(completionHandler: (Data?, (any Error)?) -> Void)](cssearchableindex/fetchlastclientstate(completionhandler:).md)
  Fetches the app’s most recent client state information asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/beginbatch())*