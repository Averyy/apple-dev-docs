# cancelButtonBounds

**Framework**: AppKit  
**Kind**: property

The rectangle for the cancel button within the bounds of the search field.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var cancelButtonBounds: NSRect { get }
```

#### Discussion

Subclasses can override `cancelButtonBounds` for custom layout purposes.

## See Also

- [var searchButtonBounds: NSRect](nssearchfield/searchbuttonbounds.md)
  The rectangle for the search button within the bounds of the search field.
- [var searchTextBounds: NSRect](nssearchfield/searchtextbounds.md)
  The rectangle for the search text within the bounds of the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/cancelbuttonbounds)*