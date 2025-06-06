# delegate

**Framework**: AppKit  
**Kind**: property

A custom object you use to manage interactions with an open or save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSOpenSavePanelDelegate)? { get set }
```

## See Also

- [protocol NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/delegate)*