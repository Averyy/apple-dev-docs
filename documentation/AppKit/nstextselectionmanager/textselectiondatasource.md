# textSelectionDataSource

**Framework**: AppKit  
**Kind**: property

The data source that provides text layout information to the selection manager.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
weak var textSelectionDataSource: (any NSTextSelectionDataSource)? { get set }
```

#### Discussion

The data source is typically an `NSTextLayoutManager` or similar text layout object.

## See Also

- [var textSelectionMode: NSTextSelectionManager.Mode](nstextselectionmanager/textselectionmode.md)
  The interaction mode for text selection.
- [NSTextSelectionManager.Mode](nstextselectionmanager/mode.md)
  Values for text selection interaction modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/textselectiondatasource)*