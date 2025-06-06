# ContactItemPage

**Framework**: ContactProvider  
**Kind**: struct

A fixed offset into enumerating all contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct ContactItemPage
```

#### Overview

You can break an enumeration of all contact items into multiple pages to reduce the memory constraints on the system. During the enumeration, the [`generationMarker`](contactitempage/generationmarker.md) must not change. Update the [`offset`](contactitempage/offset.md) to reflect progress so you can resume the enumeration.

## Topics

### Creating a contact item page
- [init(generationMarker: Data, offset: Int)](contactitempage/init(generationmarker:offset:).md)
  Creates a contact item page with the given generation marker and offset.
### Supporting paging
- [var generationMarker: Data](contactitempage/generationmarker.md)
  A value specific to your data source identifying the database generation when enumeration of content started.
- [var offset: Int](contactitempage/offset.md)
  An offset from the page’s generation marker.
- [static let initialPage: ContactItemPage](contactitempage/initialpage.md)
  A static value the system uses to indicate the start of a new content enumeration.
### Encoding and decoding
- [init(from: any Decoder) throws](contactitempage/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](contactitempage/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing contact item pages
- [static func == (ContactItemPage, ContactItemPage) -> Bool](contactitempage/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](contactitempage/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func didFinishEnumeratingContent(upTo: Data)](contactitemcontentobserver/didfinishenumeratingcontent(upto:).md)
  Finishes the content enumeration to the observer.
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](contactitemcontentobserver/didfinishenumeratingpage(upto:).md)
  Marks a page of items as completed.
- [func didFinishEnumeratingContentWithError(any Error)](contactitemcontentobserver/didfinishenumeratingcontentwitherror(_:).md)
  Finishes the content enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitempage)*