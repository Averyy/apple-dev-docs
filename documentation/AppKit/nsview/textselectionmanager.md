# textSelectionManager

**Framework**: AppKit  
**Kind**: property

The text selection manager for this view.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var textSelectionManager: NSTextSelectionManager? { get set }
```

#### Discussion

Setting this property installs gesture recognizers and configures the view to handle text selection interactions. Setting it to `nil` removes text selection support. The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/textselectionmanager)*