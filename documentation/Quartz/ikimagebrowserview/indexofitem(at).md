# indexOfItem(at:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the index of the item at the specified location.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func indexOfItem(at point: NSPoint) -> Int
```

```objc
- (NSInteger) indexOfItemAtPoint:(NSPoint) point;
```

#### Return Value

The index of the item or `NSNotFound` if no item at this location.

## Parameters

- `point`: The location of the item.

## See Also

### Getting Item Information
- [func itemFrame(at: Int) -> NSRect](./itemframe%28at%29.md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](./visibleitemindexes%28%29.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](./cellforitem%28at%29.md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/indexofitem(at:))*