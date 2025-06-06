# delegate

**Framework**: AppKit  
**Kind**: property

The tab view’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSTabViewDelegate)? { get set }
```

#### Discussion

The value of this property must conform to the [`NSTabViewDelegate`](nstabviewdelegate.md) protocol.

## See Also

- [protocol NSTabViewDelegate](nstabviewdelegate.md)
  The `NSTabViewDelegate` protocol defines the optional methods implemented by delegates of `NSTabView` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/delegate)*