# itemFrame(at:)

**Framework**: Quartz  
**Kind**: method

Returns the frame rectangle for the item located at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func itemFrame(at index: Int) -> NSRect
```

#### Return Value

The frame rectangle of the item.

## Parameters

- `index`: The index of the item whose frame rectangle you want to obtain.

## See Also

- [func indexOfItem(at: NSPoint) -> Int](ikimagebrowserview/indexofitem(at:).md)
  Returns the index of the item at the specified location.
- [func visibleItemIndexes() -> IndexSet!](ikimagebrowserview/visibleitemindexes.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](ikimagebrowserview/cellforitem(at:).md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/itemframe(at:))*