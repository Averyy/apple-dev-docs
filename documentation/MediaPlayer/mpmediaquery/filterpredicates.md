# filterPredicates

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The media property predicates of the media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var filterPredicates: Set<MPMediaPredicate>? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSSet<MPMediaPredicate *> * filterPredicates;
```

#### Discussion

The General Media Item Property Keys and Podcast Item Property Keys enumerations in [`MPMediaItem`](../mpmediaitem.md) contain the keys you can use to construct predicates.

## See Also

### Configuring media queries
- [func addFilterPredicate(MPMediaPredicate)](./addfilterpredicate%28_%29.md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](./removefilterpredicate%28_%29.md)
  Removes a filter predicate from a query.
- [var groupingType: MPMediaGrouping](./groupingtype.md)
  The grouping for collections retrieved with the media query.
- [var itemSections: [MPMediaQuerySection]?](./itemsections.md)
  An array representing the section grouping of the query’s specified media items.
- [var collectionSections: [MPMediaQuerySection]?](./collectionsections.md)
  An array representing the section grouping of the query’s specified media item collections.
- [enum MPMediaGrouping](../mpmediagrouping.md)
  Keys used to configure a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/filterpredicates)*