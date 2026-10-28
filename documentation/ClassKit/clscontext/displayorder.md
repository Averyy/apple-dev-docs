# displayOrder

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The position of a context relative to its siblings.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var displayOrder: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger displayOrder;
```

## Mentions

- [Building missing contexts](../building-missing-contexts.md)

## Discussion

Setting this value provides a hint to the system about what order you intend sibling contexts to appear in. But this has nothing to do with the order in which a teacher assigns your content. Teachers are free to assign your content in any order they choose.

## See Also

### Managing context presentation
- [var topic: CLSContextTopic?](./topic.md)
  The area of study to which a context relates.
- [struct CLSContextTopic](../clscontexttopic.md)
  The areas of study to which contexts may relate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/displayorder)*