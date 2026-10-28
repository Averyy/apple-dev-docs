# ContactItemPage

**Framework**: ContactProvider  
**Kind**: struct  
**Role**: Structure

A fixed offset into enumerating all contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct ContactItemPage
```

## Overview

You can break an enumeration of all contact items into multiple pages to reduce the memory constraints on the system. During the enumeration, the [`generationMarker`](./contactitempage/generationmarker.md) must not change. Update the [`offset`](./contactitempage/offset.md) to reflect progress so you can resume the enumeration.

## Topics

### Creating a contact item page
- [init(generationMarker: Data, offset: Int)](./contactitempage/init%28generationmarker,offset%29.md)
  Creates a contact item page with the given generation marker and offset.
### Supporting paging
- [var generationMarker: Data](./contactitempage/generationmarker.md)
  A value specific to your data source identifying the database generation when enumeration of content started.
- [var offset: Int](./contactitempage/offset.md)
  An offset from the page’s generation marker.
- [static let initialPage: ContactItemPage](./contactitempage/initialpage.md)
  A static value the system uses to indicate the start of a new content enumeration.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)

## See Also

### Ending enumeration
- [func didFinishEnumeratingContent(upTo: Data)](./contactitemcontentobserver/didfinishenumeratingcontent%28upto%29.md)
  Finishes the content enumeration to the observer.
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](./contactitemcontentobserver/didfinishenumeratingpage%28upto%29.md)
  Marks a page of items as completed.
- [func didFinishEnumeratingContentWithError(any Error)](./contactitemcontentobserver/didfinishenumeratingcontentwitherror%28_%29.md)
  Finishes the content enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitempage)*