# searchButtonRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Modifies the bounding rectangle for the search button cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func searchButtonRect(forBounds rect: NSRect) -> NSRect
```

#### Return Value

The updated bounding rectangle to use for the search button. The default value is the value passed into the `rect` parameter.

#### Discussion

Subclasses can override this method to return a new bounding rectangle for the search button cell. You might use this method to provide a custom layout for the search field control.

## Parameters

- `rect`: The current bounding rectangle for the search button.

## See Also

- [func searchTextRect(forBounds: NSRect) -> NSRect](nssearchfieldcell/searchtextrect(forbounds:).md)
  Modifies the bounding rectangle for the search-text field cell.
- [func cancelButtonRect(forBounds: NSRect) -> NSRect](nssearchfieldcell/cancelbuttonrect(forbounds:).md)
  Modifies the bounding rectangle for the cancel button cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/searchbuttonrect(forbounds:))*