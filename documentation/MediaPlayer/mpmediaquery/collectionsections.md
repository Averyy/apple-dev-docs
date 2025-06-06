# collectionSections

**Framework**: Media Player  
**Kind**: property

An array representing the section grouping of the query’s specified media item collections.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var collectionSections: [MPMediaQuerySection]? { get }
```

#### Discussion

The value of this property may be `nil` if there’s no appropriate section grouping of the media item collections.

## See Also

- [var filterPredicates: Set<MPMediaPredicate>?](mpmediaquery/filterpredicates.md)
  The media property predicates of the media query.
- [func addFilterPredicate(MPMediaPredicate)](mpmediaquery/addfilterpredicate(_:).md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](mpmediaquery/removefilterpredicate(_:).md)
  Removes a filter predicate from a query.
- [var groupingType: MPMediaGrouping](mpmediaquery/groupingtype.md)
  The grouping for collections retrieved with the media query.
- [var itemSections: [MPMediaQuerySection]?](mpmediaquery/itemsections.md)
  An array representing the section grouping of the query’s specified media items.
- [enum MPMediaGrouping](mpmediagrouping.md)
  Keys used to configure a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/collectionsections)*