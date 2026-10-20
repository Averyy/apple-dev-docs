# scrollColumnToVisible(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the view so the specified column is visible.

**Availability**:
- macOS

## Declaration

```swift
func scrollColumnToVisible(_ column: Int)
```

```objc
- (void) scrollColumnToVisible:(NSInteger) column;
```

## Parameters

- `column`: The index of the column in the [`tableColumns`](./tablecolumns.md) array.

## See Also

### Related Documentation
- [func scroll(to: NSPoint)](../nsclipview/scroll%28to%29.md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
### Scrolling
- [func scrollRowToVisible(Int)](./scrollrowtovisible%28_%29.md)
  Scrolls the view so the specified row is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/scrollcolumntovisible(_:))*