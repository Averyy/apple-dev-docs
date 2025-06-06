# MPMediaPredicate

**Framework**: Media Player  
**Kind**: class

An abstract class that defines classes for filtering media in a media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaPredicate
```

#### Overview

In media queries, a  is a statement of a logical condition that you want to test each media item against. The system returns the media items that satisfy the condition in the query result. Use this class’s concrete subclass, described in [`MPMediaPropertyPredicate`](mpmediapropertypredicate.md), to define the filter in a media query to retrieve a subset of media items from the library. For more information about media queries, see [`MPMediaQuery`](mpmediaquery.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPMediaPropertyPredicate](mpmediapropertypredicate.md)
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
- [class MPMediaPropertyPredicate](mpmediapropertypredicate.md)
  A set of predicates for defining a filter in a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapredicate)*