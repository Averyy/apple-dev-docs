# delegate

**Framework**: AppKit  
**Kind**: property

Sets the receiver’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSComboBoxDelegate)? { get set }
```

## Parameters

- `anObject`: The delegate for the receiver. The delegate must conform to the [`NSComboBoxDelegate`](nscomboboxdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/delegate)*