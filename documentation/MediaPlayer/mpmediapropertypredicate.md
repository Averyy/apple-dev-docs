# MPMediaPropertyPredicate

**Framework**: Media Player  
**Kind**: class

A set of predicates for defining a filter in a media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaPropertyPredicate
```

#### Overview

Use one or more `MPMediaPropertyPredicate` objects to define the filter in a media query to retrieve a subset of media items from the Music library. A predicate in this context is a statement of a logical condition that you want to test each media item against. The query retrieves the items that satisfy that condition.

You define Music library queries, and retrieve query results, using the [`MPMediaQuery`](mpmediaquery.md) class. [`MPMediaItem`](mpmediaitem.md) and [`MPMediaItemCollection`](mpmediaitemcollection.md) describe the media items and media item collections that you can retrieve with a query.

## Topics

### Creating media property predicates
- [init(value: Any?, forProperty: String)](mpmediapropertypredicate/init(value:forproperty:).md)
  Creates a media property predicate with the default comparison type.
- [init(value: Any?, forProperty: String, comparisonType: MPMediaPredicateComparison)](mpmediapropertypredicate/init(value:forproperty:comparisontype:).md)
  Creates a media property predicate with a specified comparison type.
### Examining media property predicates
- [var property: String](mpmediapropertypredicate/property.md)
  The property that the media property predicate uses when you invoke a query.
- [var value: Any?](mpmediapropertypredicate/value.md)
  The value that the media property predicate matches against when you invoke a query.
- [var comparisonType: MPMediaPredicateComparison](mpmediapropertypredicate/comparisontype.md)
  The type of matching comparison that the media property predicate performs when you invoke a query.
### Supporting types
- [enum MPMediaPredicateComparison](mpmediapredicatecomparison.md)
  Logical comparison types for media queries.

## Relationships

### Inherits From
- [MPMediaPredicate](mpmediapredicate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using filters to create specialized queries](using-filters-to-create-specialized-queries.md)
  Add a filter set to a query before populating a music player queue.
- [class MPMediaQuery](mpmediaquery.md)
  A query that specifies a set of media items from the device’s media library using a filter and a grouping type.
- [class MPMediaQuerySection](mpmediaquerysection.md)
  A range of media items or media item collections from within a media query.
- [class MPMediaPredicate](mpmediapredicate.md)
  An abstract class that defines classes for filtering media in a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate)*