# ContactItemSyncAnchor

**Framework**: ContactProvider  
**Kind**: struct

A snapshot point into enumerating changed contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct ContactItemSyncAnchor
```

#### Overview

You can break an enumeration of changes into batches with multiple anchors to reduce the memory constraints on the system. During enumeration, you may update the `generationMarker` and `offset` to reflect progress enumerating the changes as they occurred, possibly across mutiple database generations and how many changes occurred within each database generation.

## Topics

### Creating a sync anchor
- [init(generationMarker: Data, offset: Int)](contactitemsyncanchor/init(generationmarker:offset:).md)
  Creates a sync anchor with the given generation marker and offset.
### Inspecting sync anchor properties
- [var generationMarker: Data](contactitemsyncanchor/generationmarker.md)
  A value specific to your data source identifying the database generation you’re enumerating for changes.
- [var offset: Int](contactitemsyncanchor/offset.md)
  An offset from the anchor’s generation marker.
### Encoding and decoding
- [init(from: any Decoder) throws](contactitemsyncanchor/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (ContactItemSyncAnchor, ContactItemSyncAnchor) -> Bool](contactitemsyncanchor/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](contactitemsyncanchor/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](contactitemsyncanchor/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func didFinishEnumeratingChanges(upTo: ContactItemSyncAnchor, moreComing: Bool)](contactitemchangeobserver/didfinishenumeratingchanges(upto:morecoming:).md)
  Marks a sync anchor of changed contact items as completed.
- [func didFinishEnumeratingChangesWithError(any Error)](contactitemchangeobserver/didfinishenumeratingchangeswitherror(_:).md)
  Finishes the change enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemsyncanchor)*