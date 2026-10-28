# noteNumberOfItemsChanged()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the number of items in its data source has changed.

**Availability**:
- macOS

## Declaration

```swift
func noteNumberOfItemsChanged()
```

```objc
- (void) noteNumberOfItemsChanged;
```

## Discussion

This method allows the receiver to update the scrollers in its displayed pop-up list without actually reloading data into the receiver. It is particularly useful for a data source that continually receives data in the background over a period of time, in which case the `NSComboBox` can remain responsive to the user while the data is received.

See the NSComboBoxDataSource informal protocol specification for information on the messages an `NSComboBox` sends to its data source.

## See Also

### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func itemObjectValue(at: Int) -> Any](./itemobjectvalue%28at%29.md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/notenumberofitemschanged())*