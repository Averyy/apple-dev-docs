# generationMarker

**Framework**: ContactProvider  
**Kind**: property

A value specific to your data source identifying the database generation when enumeration of content started.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var generationMarker: Data
```

#### Discussion

When a content enumeration is underway, you must use the same `generationMarker` until the enumeration completes. If you restart content enumeration, you can use a new `generationMarker` value from that point onward.

## See Also

- [var offset: Int](contactitempage/offset.md)
  An offset from the page’s generation marker.
- [static let initialPage: ContactItemPage](contactitempage/initialpage.md)
  A static value the system uses to indicate the start of a new content enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitempage/generationmarker)*