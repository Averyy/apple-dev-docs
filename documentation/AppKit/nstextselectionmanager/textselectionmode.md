# textSelectionMode

**Framework**: AppKit  
**Kind**: property

The interaction mode for text selection.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var textSelectionMode: NSTextSelectionManager.Mode { get set }
```

#### Discussion

Determines whether text is editable, selectable only, or non-interactive. The default value is `NSTextSelectionModeEditable`.

## See Also

- [NSTextSelectionManager.Mode](nstextselectionmanager/mode.md)
  Values for text selection interaction modes.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](nstextselectionmanager/textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/textselectionmode)*