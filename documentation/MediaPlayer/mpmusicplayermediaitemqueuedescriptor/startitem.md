# startItem

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, nullable) MPMediaItem * startItem;
```

## Discussion

When this property isn’t set, the value is [`nil`](../../ObjectiveC/nil-227m0.md) and the first item in the queue is the first item to play.

## See Also

### Media item queue descriptor properties
- [var itemCollection: MPMediaItemCollection](./itemcollection.md)
  Contains the media item collection used to create the queue descriptor.
- [var query: MPMediaQuery](./query.md)
  Contains the media items found by the query used to create the queue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/startitem)*