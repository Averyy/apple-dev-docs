# delegate

**Framework**: AppKit  
**Kind**: property

The object you use to customize the toolbar contents and configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSToolbarDelegate)? { get set }
```

#### Discussion

Assign an object to this property if you customize the toolbar’s behavior. The object you assign to this property must adopt the [`NSToolbarDelegate`](nstoolbardelegate.md) protocol.

## See Also

- [protocol NSToolbarDelegate](nstoolbardelegate.md)
  A set of optional methods you use to configure the toolbar and respond to changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/delegate)*