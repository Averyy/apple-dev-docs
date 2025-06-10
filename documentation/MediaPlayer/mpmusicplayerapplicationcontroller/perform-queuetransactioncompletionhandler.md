# perform(queueTransaction:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Changes the contents of the media items in the queue.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func perform(queueTransaction: @escaping (MPMusicPlayerControllerMutableQueue) -> Void) async throws -> MPMusicPlayerControllerQueue
```

#### Discussion

Perform all of your queue modifications inside of the queue transition block. After the system modifies the queue inside of the queue transition block, it returns the new queue from the completion handler after the user accepts the new queue. Don’t access the completion handler’s queue outside of the completion handler.

If you modify the queue outside of the completion handler, register for the [`MPMusicPlayerControllerQueueDidChangeNotification`](mpmusicplayercontrollerqueuedidchangenotification.md) notification and ensure your app responds accordingly.

## Parameters

- `queueTransaction`: A block that the system calls while it creates the queue.
- `completionHandler`: A block that the system calls after the user accepts the new queue.

## See Also

- [static let MPMusicPlayerControllerQueueDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/MPMusicPlayerControllerQueueDidChange.md)
  Indicates the music player’s queue changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerapplicationcontroller/perform(queuetransaction:completionhandler:))*