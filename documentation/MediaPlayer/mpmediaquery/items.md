# items

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

An array of media items that match the media query’s predicate.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var items: [MPMediaItem]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<MPMediaItem *> * items;
```

#### Discussion

If no items match the predicate, this method returns an empty array. On error, returns `nil`.

## See Also

### Performing media queries
- [var collections: [MPMediaItemCollection]?](./collections.md)
  An array of media item collections whose contained items match the query’s media property predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/items)*