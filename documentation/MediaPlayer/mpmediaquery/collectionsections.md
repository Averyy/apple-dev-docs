# collectionSections

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSArray<MPMediaQuerySection *> * collectionSections;
```

#### Discussion

The value of this property may be `nil` if there’s no appropriate section grouping of the media item collections.

## See Also

### Configuring media queries
- [var filterPredicates: Set<MPMediaPredicate>?](./filterpredicates.md)
  The media property predicates of the media query.
- [func addFilterPredicate(MPMediaPredicate)](./addfilterpredicate%28_%29.md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](./removefilterpredicate%28_%29.md)
  Removes a filter predicate from a query.
- [var groupingType: MPMediaGrouping](./groupingtype.md)
  The grouping for collections retrieved with the media query.
- [var itemSections: [MPMediaQuerySection]?](./itemsections.md)
  An array representing the section grouping of the query’s specified media items.
- [enum MPMediaGrouping](../mpmediagrouping.md)
  Keys used to configure a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/collectionsections)*