# suggestionsDelegate

**Framework**: AppKit  
**Kind**: property

The delegate that provides text suggestions for the receiving text field and responds to the user highlighting and selecting items.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var suggestionsDelegate: (any NSTextSuggestionsDelegate)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/suggestionsdelegate)*