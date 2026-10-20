# init(layoutSize:elementKind:alignment:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment)
```

```objc
+ (instancetype) boundarySupplementaryItemWithLayoutSize:(NSCollectionLayoutSize *) layoutSize elementKind:(NSString *) elementKind alignment:(NSRectAlignment) alignment;
```

## See Also

### Creating a boundary supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment, absoluteOffset: CGPoint)](./init%28layoutsize,elementkind,alignment,absoluteoffset%29.md)
  Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout at an absolute offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutboundarysupplementaryitem/init(layoutsize:elementkind:alignment:))*