# delegate

**Framework**: AppKit  
**Kind**: property

The outline view’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSOutlineViewDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NSOutlineViewDelegate`](nsoutlineviewdelegate.md) protocol. Note that in versions of macOS prior to v10.12, the table view did not retain the delegate in a managed memory environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/delegate)*