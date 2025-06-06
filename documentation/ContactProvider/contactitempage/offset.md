# offset

**Framework**: ContactProvider  
**Kind**: property

An offset from the page’s generation marker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var offset: Int
```

#### Discussion

You can use the offset to track a contiguous number of contact items which have been successfully enumerated for that database generation.

## See Also

- [var generationMarker: Data](contactitempage/generationmarker.md)
  A value specific to your data source identifying the database generation when enumeration of content started.
- [static let initialPage: ContactItemPage](contactitempage/initialpage.md)
  A static value the system uses to indicate the start of a new content enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitempage/offset)*