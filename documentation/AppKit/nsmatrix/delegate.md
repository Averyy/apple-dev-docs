# delegate

**Framework**: AppKit  
**Kind**: property

The delegate for messages from the field editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSMatrixDelegate)? { get set }
```

## See Also

- [func textShouldEndEditing(NSText) -> Bool](nsmatrix/textshouldendediting(_:).md)
  Requests permission to end editing.
- [func textShouldBeginEditing(NSText) -> Bool](nsmatrix/textshouldbeginediting(_:).md)
  Requests permission to begin editing text.
- [protocol NSMatrixDelegate](nsmatrixdelegate.md)
  The `NSMatrixDelegate` protocol defines the optional methods implemented by delegates of `NSMatrix` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/delegate)*