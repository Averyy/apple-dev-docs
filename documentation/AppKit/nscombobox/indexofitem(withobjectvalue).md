# indexOfItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches the receiver’s internal item list for the specified object and returns the lowest matching index.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withObjectValue object: Any) -> Int
```

```objc
- (NSInteger) indexOfItemWithObjectValue:(id) object;
```

#### Return Value

The lowest index in the internal item list whose corresponding value is equal to that of the specified object. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](../../Swift/true.md).

#### Discussion

If none of the objects in the receiver’s internal item list are equal to `anObject`, [`indexOfItem(withObjectValue:)`](./indexofitem%28withobjectvalue%29.md) returns `NSNotFound`.

#### Discussion

This method logs a warning if the [`usesDataSource`](./usesdatasource.md) property is [`true`](../../Swift/true.md).

## Parameters

- `object`: The object for which to return the index.

## See Also

### Related Documentation
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the given object.
### Manipulating the Displayed List
- [func itemObjectValue(at: Int) -> Any](./itemobjectvalue%28at%29.md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the receiver that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/indexofitem(withobjectvalue:))*