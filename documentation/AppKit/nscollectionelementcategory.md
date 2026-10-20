# NSCollectionElementCategory

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants specifying the type of element in the collection view.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.11+

## Declaration

```swift
enum NSCollectionElementCategory
```

```c
enum NSCollectionElementCategory : NSInteger;
```

## Topics

### Constants
- [NSCollectionElementCategory.item](./nscollectionelementcategory/item.md)
  The element is an item. Items represent the main content of your collection view.
- [NSCollectionElementCategory.supplementaryView](./nscollectionelementcategory/supplementaryview.md)
  The element is a supplementary view. Use supplementary views for single views that contain some data but are associated with an entire section. For example, use them to specify header or footer views for a section.
- [NSCollectionElementCategory.decorationView](./nscollectionelementcategory/decorationview.md)
  The element is a decoration view. Decoration views represent visual adornments that do not contain any data of their own.
- [NSCollectionElementCategory.interItemGap](./nscollectionelementcategory/interitemgap.md)
  The element is an inter-item gap. An inter-item gap element is a custom visual indicator that is displayed between items when dropping items into the collection view.
### Initializers
- [init?(rawValue: Int)](./nscollectionelementcategory/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Inter-Item Gap Support](./inter-item-gap-support.md)
  Constant for supporting inter-item gaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionelementcategory)*