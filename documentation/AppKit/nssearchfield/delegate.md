# delegate

**Framework**: AppKit  
**Kind**: property

The delegate for the search field, or `nil` if the search field doesn’t have a delegate.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
weak var delegate: (any NSSearchFieldDelegate)? { get set }
```

## See Also

- [protocol NSSearchFieldDelegate](nssearchfielddelegate.md)
  A protocol that a search field delegate can use to determine when a search started or ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/delegate)*