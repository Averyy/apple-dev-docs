# reloadItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reloads and redisplays the data for the given item.

**Availability**:
- macOS

## Declaration

```swift
func reloadItem(_ item: Any?)
```

```objc
- (void) reloadItem:(id) item;
```

## Discussion

Reloading the cell views associated with `item` occurs only in apps that link against macOS 10.12 and later.

This method may cause the outline view to change its selection without calling the [`outlineViewSelectionDidChange(_:)`](../nsoutlineviewdelegate/outlineviewselectiondidchange%28_%29.md) delegate method.

## Parameters

- `item`: The item to reload and display.

## See Also

### Redisplaying Information
- [func reloadItem(Any?, reloadChildren: Bool)](./reloaditem%28_,reloadchildren%29.md)
  Reloads a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/reloaditem(_:))*