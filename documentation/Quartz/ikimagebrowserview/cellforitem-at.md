# cellForItem(at:)

**Framework**: Quartz  
**Kind**: method

Returns the browser cell for the item at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func cellForItem(at index: Int) -> IKImageBrowserCell!
```

#### Return Value

The browser cell at the specified index.

#### Discussion

Subclasses must not override this method.

## Parameters

- `index`: The index.

## See Also

- [func indexOfItem(at: NSPoint) -> Int](ikimagebrowserview/indexofitem(at:).md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](ikimagebrowserview/itemframe(at:).md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](ikimagebrowserview/visibleitemindexes.md)
  Returns the indexes of the view’s currently visible items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/cellforitem(at:))*