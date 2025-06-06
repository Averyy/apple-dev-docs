# startItem

**Framework**: Media Player  
**Kind**: property

Designates the media item to play first.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var startItem: MPMediaItem? { get set }
```

#### Discussion

When this property isn’t set, the value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) and the first item in the queue is the first item to play.

## See Also

- [var itemCollection: MPMediaItemCollection](mpmusicplayermediaitemqueuedescriptor/itemcollection.md)
  Contains the media item collection used to create the queue descriptor.
- [var query: MPMediaQuery](mpmusicplayermediaitemqueuedescriptor/query.md)
  Contains the media items found by the query used to create the queue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/startitem)*