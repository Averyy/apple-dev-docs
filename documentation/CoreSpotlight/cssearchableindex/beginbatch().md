# beginBatch()

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) beginIndexBatch;
```

#### Discussion

Don’t call this method again before [`endBatch(withClientState:completionHandler:)`](./endbatch%28withclientstate,completionhandler%29.md) has returned. (You can call it again before the completion handler passed to [`endBatch(withClientState:completionHandler:)`](./endbatch%28withclientstate,completionhandler%29.md) has been called.)

## See Also

### Batching index updates
- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](./endbatch%28withclientstate,completionhandler%29.md)
  Ends a batch of index updates and stores the specified state information.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](./endindexbatch%28expectedclientstate,newclientstate,completionhandler%29.md)
  Ends a batch of index updates and stores the specified state information.
- [func fetchLastClientState(completionHandler: (Data?, (any Error)?) -> Void)](./fetchlastclientstate%28completionhandler%29.md)
  Fetches the app’s most recent client state information asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/beginbatch())*