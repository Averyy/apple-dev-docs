# searchTextBounds

**Framework**: AppKit  
**Kind**: property

The rectangle for the search text within the bounds of the search field.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var searchTextBounds: NSRect { get }
```

#### Discussion

Subclasses can override `searchTextBounds` for custom layout purposes.

## See Also

- [var cancelButtonBounds: NSRect](nssearchfield/cancelbuttonbounds.md)
  The rectangle for the cancel button within the bounds of the search field.
- [var searchButtonBounds: NSRect](nssearchfield/searchbuttonbounds.md)
  The rectangle for the search button within the bounds of the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/searchtextbounds)*