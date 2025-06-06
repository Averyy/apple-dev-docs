# MPMediaQuerySection

**Framework**: Media Player  
**Kind**: class

A range of media items or media item collections from within a media query.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaQuerySection
```

#### Overview

You can use sections when displaying a query’s items or collections in your app’s user interface. You obtain an array of media query sections by using the [`itemSections`](mpmediaquery/itemsections.md) or [`collectionSections`](mpmediaquery/collectionsections.md) properties of a media query (an instance of the [`MPMediaQuery`](mpmediaquery.md) class). The property values of a media query section are read-only.

## Topics

### Working with media query sections
- [var title: String](mpmediaquerysection/title.md)
  The localized title of the media query section.
- [var range: NSRange](mpmediaquerysection/range.md)
  The range in the media query’s items or collections array that the media query section represents.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using filters to create specialized queries](using-filters-to-create-specialized-queries.md)
  Add a filter set to a query before populating a music player queue.
- [class MPMediaQuery](mpmediaquery.md)
  A query that specifies a set of media items from the device’s media library using a filter and a grouping type.
- [class MPMediaPropertyPredicate](mpmediapropertypredicate.md)
  A set of predicates for defining a filter in a media query.
- [class MPMediaPredicate](mpmediapredicate.md)
  An abstract class that defines classes for filtering media in a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)*