# newCell(forRepresentedItem:)

**Framework**: Quartz  
**Kind**: method

Returns the cell to use for the specified item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func newCell(forRepresentedItem anItem: Any!) -> IKImageBrowserCell!
```

#### Return Value

A new cell.

#### Discussion

Subclasses can override this method to customize the appearance of the cell that will represent `anItem`.

## Parameters

- `anItem`: The item that the returned cell will represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/newcell(forrepresenteditem:))*