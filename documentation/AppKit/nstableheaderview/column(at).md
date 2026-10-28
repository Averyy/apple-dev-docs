# column(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the column whose header lies under `aPoint` in the receiver, or –1 if no such column is found.

**Availability**:
- macOS

## Declaration

```swift
func column(at point: NSPoint) -> Int
```

```objc
- (NSInteger) columnAtPoint:(NSPoint) point;
```

## Discussion

`aPoint` is expressed in the receiver’s coordinate system.

## See Also

### Utility methods
- [func headerRect(ofColumn: Int) -> NSRect](./headerrect%28ofcolumn%29.md)
  Returns the rectangle containing the header tile for the column at `columnIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/column(at:))*