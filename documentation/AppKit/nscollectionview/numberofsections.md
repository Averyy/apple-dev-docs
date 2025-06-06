# numberOfSections

**Framework**: AppKit  
**Kind**: property

The number of sections in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var numberOfSections: Int { get }
```

#### Discussion

This property contains the number of sections reported by the data source object. If the collection view does not use a data source object, the value in this property is `1`.

## See Also

- [func numberOfItems(inSection: Int) -> Int](nscollectionview/numberofitems(insection:).md)
  Returns the number of items in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/numberofsections)*