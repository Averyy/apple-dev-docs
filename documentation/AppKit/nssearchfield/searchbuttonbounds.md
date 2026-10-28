# searchButtonBounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle for the search button within the bounds of the search field.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var searchButtonBounds: NSRect { get }
```

```objc
@property (readonly) NSRect searchButtonBounds;
```

## Discussion

Subclasses can override `searchButtonBounds` for custom layout purposes.

## See Also

### Getting Search Field Metrics
- [var cancelButtonBounds: NSRect](./cancelbuttonbounds.md)
  The rectangle for the cancel button within the bounds of the search field.
- [var searchTextBounds: NSRect](./searchtextbounds.md)
  The rectangle for the search text within the bounds of the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/searchbuttonbounds)*