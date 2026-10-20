# query

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

Contains the media items found by the query used to create the queue descriptor.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var query: MPMediaQuery { get }
```

```objc
@property (nonatomic, copy, readonly) MPMediaQuery * query;
```

## See Also

### Media item queue descriptor properties
- [var itemCollection: MPMediaItemCollection](./itemcollection.md)
  Contains the media item collection used to create the queue descriptor.
- [var startItem: MPMediaItem?](./startitem.md)
  Designates the media item to play first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/query)*