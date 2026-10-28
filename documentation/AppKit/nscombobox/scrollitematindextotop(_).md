# scrollItemAtIndexToTop(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.

**Availability**:
- macOS

## Declaration

```swift
func scrollItemAtIndexToTop(_ index: Int)
```

```objc
- (void) scrollItemAtIndexToTop:(NSInteger) index;
```

## Discussion

The pop-up list need not be displayed at the time this method is invoked.

## Parameters

- `index`: The index of the item to scroll to the top.

## See Also

### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func itemObjectValue(at: Int) -> Any](./itemobjectvalue%28at%29.md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the receiver that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/scrollitematindextotop(_:))*