# canReorderItemHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The handler that determines whether you can reorder a particular item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) BOOL (^canReorderItemHandler)(ItemType );
```

## See Also

### Reordering items
- [willReorderHandler](./willreorderhandler.md)
  The handler that prepares the diffable data source for reordering its items.
- [didReorderHandler](./didreorderhandler.md)
  The handler that processes a reordering transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/canreorderitemhandler)*