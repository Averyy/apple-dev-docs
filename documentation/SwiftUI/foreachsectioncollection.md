# ForEachSectionCollection

**Framework**: SwiftUI  
**Kind**: struct

A collection which allows a view to be treated as a collection of its sections in a for each loop.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ForEachSectionCollection<Content> where Content : View
```

#### Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sequence](../swift/sequence.md)

## See Also

- [struct ForEach](foreach.md)
  A structure that computes views on demand from an underlying collection of identified data.
- [struct ForEachSubviewCollection](foreachsubviewcollection.md)
  A collection which allows a view to be treated as a collection of its subviews in a for each loop.
- [protocol DynamicViewContent](dynamicviewcontent.md)
  A type of view that generates views from an underlying collection of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreachsectioncollection)*