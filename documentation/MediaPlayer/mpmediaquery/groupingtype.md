# groupingType

**Framework**: Media Player  
**Kind**: property

The grouping for collections retrieved with the media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var groupingType: MPMediaGrouping { get set }
```

#### Discussion

The default grouping type is [`MPMediaGrouping.title`](mpmediagrouping/title.md). See [`MPMediaGrouping`](mpmediagrouping.md) for the list of available grouping types.

## See Also

- [var filterPredicates: Set<MPMediaPredicate>?](mpmediaquery/filterpredicates.md)
  The media property predicates of the media query.
- [func addFilterPredicate(MPMediaPredicate)](mpmediaquery/addfilterpredicate(_:).md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](mpmediaquery/removefilterpredicate(_:).md)
  Removes a filter predicate from a query.
- [var itemSections: [MPMediaQuerySection]?](mpmediaquery/itemsections.md)
  An array representing the section grouping of the query’s specified media items.
- [var collectionSections: [MPMediaQuerySection]?](mpmediaquery/collectionsections.md)
  An array representing the section grouping of the query’s specified media item collections.
- [enum MPMediaGrouping](mpmediagrouping.md)
  Keys used to configure a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/groupingtype)*