# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A custom object you use to manage interactions with an open or save panel.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSOpenSavePanelDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSOpenSavePanelDelegate> delegate;
```

## See Also

### Responding to User Interactions
- [protocol NSOpenSavePanelDelegate](../nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/delegate)*