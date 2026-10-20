# init(layoutSize:elementKind:alignment:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment)
```

```objc
+ (instancetype) boundarySupplementaryItemWithLayoutSize:(NSCollectionLayoutSize *) layoutSize elementKind:(NSString *) elementKind alignment:(NSRectAlignment) alignment;
```

## See Also

### Creating a boundary supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment, absoluteOffset: NSPoint)](./init%28layoutsize,elementkind,alignment,absoluteoffset%29.md)
  Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout at an absolute offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutboundarysupplementaryitem/init(layoutsize:elementkind:alignment:))*