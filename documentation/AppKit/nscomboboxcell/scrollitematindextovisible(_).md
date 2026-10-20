# scrollItemAtIndexToVisible(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.

**Availability**:
- macOS

## Declaration

```swift
func scrollItemAtIndexToVisible(_ index: Int)
```

```objc
- (void) scrollItemAtIndexToVisible:(NSInteger) index;
```

#### Discussion

The pop-up list need not be displayed at the time this method is invoked.

## Parameters

- `index`: The index of the item to make visible.

## See Also

### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
- [func itemObjectValue(at: Int) -> Any](./itemobjectvalue%28at%29.md)
  Returns the object located at the specified location in the internal item list.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the combo box that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/scrollitematindextovisible(_:))*