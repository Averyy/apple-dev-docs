# itemFrame(at:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the frame rectangle for the item located at the specified index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func itemFrame(at index: Int) -> NSRect
```

```objc
- (NSRect) itemFrameAtIndex:(NSInteger) index;
```

#### Return Value

The frame rectangle of the item.

## Parameters

- `index`: The index of the item whose frame rectangle you want to obtain.

## See Also

### Getting Item Information
- [func indexOfItem(at: NSPoint) -> Int](./indexofitem%28at%29.md)
  Returns the index of the item at the specified location.
- [func visibleItemIndexes() -> IndexSet!](./visibleitemindexes%28%29.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](./cellforitem%28at%29.md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/itemframe(at:))*