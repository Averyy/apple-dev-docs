# ContactItemSyncAnchor

**Framework**: ContactProvider  
**Kind**: struct  
**Role**: Structure

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
- [init(generationMarker: Data, offset: Int)](./contactitemsyncanchor/init%28generationmarker,offset%29.md)
  Creates a sync anchor with the given generation marker and offset.
### Inspecting sync anchor properties
- [var generationMarker: Data](./contactitemsyncanchor/generationmarker.md)
  A value specific to your data source identifying the database generation you’re enumerating for changes.
- [var offset: Int](./contactitemsyncanchor/offset.md)
  An offset from the anchor’s generation marker.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)

## See Also

### Ending enumeration
- [func didFinishEnumeratingChanges(upTo: ContactItemSyncAnchor, moreComing: Bool)](./contactitemchangeobserver/didfinishenumeratingchanges%28upto,morecoming%29.md)
  Marks a sync anchor of changed contact items as completed.
- [func didFinishEnumeratingChangesWithError(any Error)](./contactitemchangeobserver/didfinishenumeratingchangeswitherror%28_%29.md)
  Finishes the change enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemsyncanchor)*