# newCell(forRepresentedItem:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the cell to use for the specified item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func newCell(forRepresentedItem anItem: Any!) -> IKImageBrowserCell!
```

```objc
- (IKImageBrowserCell *) newCellForRepresentedItem:(id) anItem;
```

#### Return Value

A new cell.

#### Discussion

Subclasses can override this method to customize the appearance of the cell that will represent `anItem`.

## Parameters

- `anItem`: The item that the returned cell will represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/newcell(forrepresenteditem:))*