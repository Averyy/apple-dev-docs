# collections

**Framework**: Media Player  
**Kind**: property

An array of media item collections whose contained items match the query’s media property predicate.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var collections: [MPMediaItemCollection]? { get }
```

#### Discussion

The system groups and sorts the returned array of collections by the `groupingType` of the media query. The following code listing demonstrates how to use this property:

Each element of the `collections` array now contains a media item collection. Each collection contains the media items from the library by a particular artist. The system sorts elements of the array by the artist name.

For the available grouping types, see [`MPMediaGrouping`](mpmediagrouping.md).

## See Also

- [var items: [MPMediaItem]?](mpmediaquery/items.md)
  An array of media items that match the media query’s predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/collections)*