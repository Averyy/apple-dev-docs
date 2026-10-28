# searchButtonRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies the bounding rectangle for the search button cell.

**Availability**:
- macOS

## Declaration

```swift
func searchButtonRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) searchButtonRectForBounds:(NSRect) rect;
```

## Return Value

The updated bounding rectangle to use for the search button. The default value is the value passed into the `rect` parameter.

## Discussion

Subclasses can override this method to return a new bounding rectangle for the search button cell. You might use this method to provide a custom layout for the search field control.

## Parameters

- `rect`: The current bounding rectangle for the search button.

## See Also

### Custom layout
- [func searchTextRect(forBounds: NSRect) -> NSRect](./searchtextrect%28forbounds%29.md)
  Modifies the bounding rectangle for the search-text field cell.
- [func cancelButtonRect(forBounds: NSRect) -> NSRect](./cancelbuttonrect%28forbounds%29.md)
  Modifies the bounding rectangle for the cancel button cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/searchbuttonrect(forbounds:))*