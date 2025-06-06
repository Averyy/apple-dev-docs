# TVContentIdentifier

**Framework**: TV Services  
**Kind**: class

An object that uniquely identifies media content in either a single piece or a collection.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVContentIdentifier
```

#### Overview

Every content identifier is represented by two parts: a string identifier ([`identifier`](tvcontentidentifier/identifier.md)) and a container identifier ([`container`](tvcontentidentifier/container.md)). The container identifier may be `nil`, which indicates that the content lives at the top level of the container hierarchy. You are responsible for organizing your content into a hierarchy and creating identifiers that uniquely identify each piece of content.

When designing your content identifiers, follow this guidance:

- A given content identifier must be unique for a particular content item, across  past, current, and future content items, even if the user no longer has access to that item.
- The uniqueness of a content identifier comes from the uniqueness of its two parts. The [`identifier`](tvcontentidentifier/identifier.md) property of a content identifier need not be universally unique across all of the app’s content identifiers, as long as items that share the same identifier string are contained in different containers.

## Topics

### Initializing a Content Identifier
- [init(identifier: String, container: TVContentIdentifier?)](tvcontentidentifier/init(identifier:container:).md)
  Creates a new content identifier.
- [init?(coder: NSCoder)](tvcontentidentifier/init(coder:).md)
  Returns an object initialized from data in a given unarchiver.
### Inspecting an Identifier’s Contents
- [var identifier: String](tvcontentidentifier/identifier.md)
  The string that identifies this content item.
- [var container: TVContentIdentifier?](tvcontentidentifier/container.md)
  The container that this content item is contained in.

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

- [class TVContentItem](tvcontentitem.md)
  An object that describes either a piece of content or a container for other content items.
- [func TVTopShelfImageSize(shape: TVContentItemImageShape, style: TVTopShelfContentStyle) -> CGSize](tvtopshelfimagesize(shape:style:).md)
  Returns the ideal size for an image, according to its particular shape and style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentidentifier)*