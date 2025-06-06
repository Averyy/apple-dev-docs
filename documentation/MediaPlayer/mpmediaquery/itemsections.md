# itemSections

**Framework**: Media Player  
**Kind**: property

An array representing the section grouping of the query’s specified media items.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var itemSections: [MPMediaQuerySection]? { get }
```

#### Discussion

This property consists of an array of [`MPMediaQuerySection`](mpmediaquerysection.md) instances. The value of this property may be `nil` if there’s no appropriate section grouping of the media items.

## See Also

- [var filterPredicates: Set<MPMediaPredicate>?](mpmediaquery/filterpredicates.md)
  The media property predicates of the media query.
- [func addFilterPredicate(MPMediaPredicate)](mpmediaquery/addfilterpredicate(_:).md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](mpmediaquery/removefilterpredicate(_:).md)
  Removes a filter predicate from a query.
- [var groupingType: MPMediaGrouping](mpmediaquery/groupingtype.md)
  The grouping for collections retrieved with the media query.
- [var collectionSections: [MPMediaQuerySection]?](mpmediaquery/collectionsections.md)
  An array representing the section grouping of the query’s specified media item collections.
- [enum MPMediaGrouping](mpmediagrouping.md)
  Keys used to configure a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/itemsections)*