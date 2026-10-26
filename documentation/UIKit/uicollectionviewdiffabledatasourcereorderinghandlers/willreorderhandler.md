# willReorderHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The handler that prepares the diffable data source for reordering its items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^willReorderHandler)(NSDiffableDataSourceTransaction<id,id> *);
```

## See Also

### Reordering items
- [canReorderItemHandler](./canreorderitemhandler.md)
  The handler that determines whether you can reorder a particular item.
- [didReorderHandler](./didreorderhandler.md)
  The handler that processes a reordering transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/willreorderhandler)*