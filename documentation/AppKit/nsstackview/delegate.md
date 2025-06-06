# delegate

**Framework**: AppKit  
**Kind**: property

The delegate object for the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
weak var delegate: (any NSStackViewDelegate)? { get set }
```

#### Discussion

The system calls a delegate method when resizing has caused a view to be detached from or reattached to the stack view. For more information, see [`NSStackViewDelegate`](nsstackviewdelegate.md).

## See Also

- [protocol NSStackViewDelegate](nsstackviewdelegate.md)
  A set of methods you use to respond to a stack view detaching and reattaching views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/delegate)*