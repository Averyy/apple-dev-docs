# visibleItemIndexes()

**Framework**: Quartz  
**Kind**: method

Returns the indexes of the view’s currently visible items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func visibleItemIndexes() -> IndexSet!
```

#### Return Value

A set containing the indexes.

## See Also

- [func indexOfItem(at: NSPoint) -> Int](ikimagebrowserview/indexofitem(at:).md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](ikimagebrowserview/itemframe(at:).md)
  Returns the frame rectangle for the item located at the specified index.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](ikimagebrowserview/cellforitem(at:).md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/visibleitemindexes())*