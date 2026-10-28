# imageBrowser(_:moveItemsAt:to:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Signals that the specified items should be moved to the specified destination.

**Availability**:
- macOS

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, moveItemsAt indexes: IndexSet!, to destinationIndex: Int) -> Bool
```

```objc
- (BOOL) imageBrowser:(IKImageBrowserView *) aBrowser moveItemsAtIndexes:(NSIndexSet *) indexes toIndex:(NSUInteger) destinationIndex;
```

## Return Value

[`YES`](../yes.md) if successful; [`NO`](../no.md) otherwise.

## Discussion

This method is optional. It is invoked by the image browser view after  Image Kit determines  that a reordering operation should be applied. The data source should update itself by reordering its elements.

## Parameters

- `aBrowser`: An image browser view.
- `indexes`: The indexes of the items that should be reordered.
- `destinationIndex`: The starting index of the destination the items should be moved to.

## See Also

### Related Documentation
- [func setAllowsReordering(Bool)](../../Quartz/ikimagebrowserview/setallowsreordering%28_%29.md)
  Controls whether the user can reorder items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:moveitemsat:to:))*