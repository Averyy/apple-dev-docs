# reloadItem(_:)

**Framework**: AppKit  
**Kind**: method

Reloads and redisplays the data for the given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadItem(_ item: Any?)
```

#### Discussion

Reloading the cell views associated with `item` occurs only in apps that link against macOS 10.12 and later.

This method may cause the outline view to change its selection without calling the [`outlineViewSelectionDidChange(_:)`](nsoutlineviewdelegate/outlineviewselectiondidchange(_:).md) delegate method.

## Parameters

- `item`: The item to reload and display.

## See Also

- [func reloadItem(Any?, reloadChildren: Bool)](nsoutlineview/reloaditem(_:reloadchildren:).md)
  Reloads a given item and, optionally, its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/reloaditem(_:))*