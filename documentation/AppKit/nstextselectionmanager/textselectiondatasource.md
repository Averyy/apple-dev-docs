# textSelectionDataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The data source that provides text layout information to the selection manager.

**Availability**:
- macOS 27.0+

## Declaration

```swift
weak var textSelectionDataSource: (any NSTextSelectionDataSource)? { get set }
```

```objc
@property (weak, nullable) id<NSTextSelectionDataSource> textSelectionDataSource;
```

## Discussion

The data source is typically an `NSTextLayoutManager` or similar text layout object.

## See Also

### Configuring text selection
- [var textSelectionMode: NSTextSelectionManager.Mode](./textselectionmode.md)
  The interaction mode for text selection.
- [NSTextSelectionManager.Mode](./mode.md)
  Values for text selection interaction modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/textselectiondatasource)*