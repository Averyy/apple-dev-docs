# shouldExpandItemHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The handler that determines whether a particular item is expandable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) BOOL (^shouldExpandItemHandler)(ItemType );
```

## See Also

### Expanding and collapsing items
- [shouldCollapseItemHandler](./shouldcollapseitemhandler.md)
  The handler that determines whether a particular item is collapsable.
- [willCollapseItemHandler](./willcollapseitemhandler.md)
  The handler that prepares the diffable data source for collapsing an item.
- [willExpandItemHandler](./willexpanditemhandler.md)
  The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParentItemHandler](./snapshotforexpandingparentitemhandler.md)
  The handler that provides the section snapshot for expanding the parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler)*