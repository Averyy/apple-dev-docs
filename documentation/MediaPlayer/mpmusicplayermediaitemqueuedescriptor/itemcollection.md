# itemCollection

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

Contains the media item collection used to create the queue descriptor.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var itemCollection: MPMediaItemCollection { get }
```

```objc
@property (nonatomic, strong, readonly) MPMediaItemCollection * itemCollection;
```

## See Also

### Media item queue descriptor properties
- [var query: MPMediaQuery](./query.md)
  Contains the media items found by the query used to create the queue descriptor.
- [var startItem: MPMediaItem?](./startitem.md)
  Designates the media item to play first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/itemcollection)*