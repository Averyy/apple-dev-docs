# init(layoutSize:elementKind:alignment:absoluteOffset:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout at an absolute offset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment, absoluteOffset: NSPoint)
```

```objc
+ (instancetype) boundarySupplementaryItemWithLayoutSize:(NSCollectionLayoutSize *) layoutSize elementKind:(NSString *) elementKind alignment:(NSRectAlignment) alignment absoluteOffset:(NSPoint) absoluteOffset;
```

## See Also

### Creating a boundary supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment)](./init%28layoutsize,elementkind,alignment%29.md)
  Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutboundarysupplementaryitem/init(layoutsize:elementkind:alignment:absoluteoffset:))*