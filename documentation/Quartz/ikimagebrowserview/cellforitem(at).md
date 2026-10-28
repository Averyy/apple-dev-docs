# cellForItem(at:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the browser cell for the item at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func cellForItem(at index: Int) -> IKImageBrowserCell!
```

```objc
- (IKImageBrowserCell *) cellForItemAtIndex:(NSUInteger) index;
```

## Return Value

The browser cell at the specified index.

## Discussion

Subclasses must not override this method.

## Parameters

- `index`: The index.

## See Also

### Getting Item Information
- [func indexOfItem(at: NSPoint) -> Int](./indexofitem%28at%29.md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](./itemframe%28at%29.md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](./visibleitemindexes%28%29.md)
  Returns the indexes of the view’s currently visible items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/cellforitem(at:))*