# visibleItemIndexes()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the indexes of the view’s currently visible items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func visibleItemIndexes() -> IndexSet!
```

```objc
- (NSIndexSet *) visibleItemIndexes;
```

## Return Value

A set containing the indexes.

## See Also

### Getting Item Information
- [func indexOfItem(at: NSPoint) -> Int](./indexofitem%28at%29.md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](./itemframe%28at%29.md)
  Returns the frame rectangle for the item located at the specified index.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](./cellforitem%28at%29.md)
  Returns the browser cell for the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/visibleitemindexes())*