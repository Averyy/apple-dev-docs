# numberOfSections

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of sections in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var numberOfSections: Int { get }
```

```objc
@property (readonly) NSInteger numberOfSections;
```

#### Discussion

This property contains the number of sections reported by the data source object. If the collection view does not use a data source object, the value in this property is `1`.

## See Also

### Getting the State of the Collection View
- [func numberOfItems(inSection: Int) -> Int](./numberofitems%28insection%29.md)
  Returns the number of items in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/numberofsections)*