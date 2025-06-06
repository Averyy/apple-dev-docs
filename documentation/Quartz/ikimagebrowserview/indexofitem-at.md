# indexOfItem(at:)

**Framework**: Quartz  
**Kind**: method

Returns the index of the item at the specified location.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func indexOfItem(at point: NSPoint) -> Int
```

#### Return Value

The index of the item or `NSNotFound` if no item at this location.

## Parameters

- `point`: The location of the item.

## See Also

- [func itemFrame(at: Int) -> NSRect](ikimagebrowserview/itemframe(at:).md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](ikimagebrowserview/visibleitemindexes.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](ikimagebrowserview/cellforitem(at:).md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/indexofitem(at:))*