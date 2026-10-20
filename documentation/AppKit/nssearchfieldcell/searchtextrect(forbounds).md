# searchTextRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies the bounding rectangle for the search-text field cell.

**Availability**:
- macOS

## Declaration

```swift
func searchTextRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) searchTextRectForBounds:(NSRect) rect;
```

#### Return Value

The updated bounding rectangle to use for the search text field. The default value is the value passed into the `rect` parameter.

#### Discussion

Subclasses can override this method to return a new bounding rectangle for the text-field cell object. You might use this method to provide a custom layout for the search field control.

## Parameters

- `rect`: The current bounding rectangle for the search text field.

## See Also

### Custom layout
- [func searchButtonRect(forBounds: NSRect) -> NSRect](./searchbuttonrect%28forbounds%29.md)
  Modifies the bounding rectangle for the search button cell.
- [func cancelButtonRect(forBounds: NSRect) -> NSRect](./cancelbuttonrect%28forbounds%29.md)
  Modifies the bounding rectangle for the cancel button cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/searchtextrect(forbounds:))*