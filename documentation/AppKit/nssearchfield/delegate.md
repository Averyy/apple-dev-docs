# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the search field, or `nil` if the search field doesn’t have a delegate.

**Availability**:
- macOS 10.11+

## Declaration

```swift
weak var delegate: (any NSSearchFieldDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSearchFieldDelegate> delegate;
```

## See Also

### Managing Search
- [protocol NSSearchFieldDelegate](../nssearchfielddelegate.md)
  A protocol that a search field delegate can use to determine when a search started or ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/delegate)*