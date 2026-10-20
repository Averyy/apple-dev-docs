# addFilterPredicate(_:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Adds a media property predicate to a query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addFilterPredicate(_ predicate: MPMediaPredicate)
```

```objc
- (void) addFilterPredicate:(MPMediaPredicate *) predicate;
```

## Parameters

- `predicate`: The media predicate to add to the set of predicates for the query.

## See Also

### Configuring media queries
- [var filterPredicates: Set<MPMediaPredicate>?](./filterpredicates.md)
  The media property predicates of the media query.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/addfilterpredicate(_:))*