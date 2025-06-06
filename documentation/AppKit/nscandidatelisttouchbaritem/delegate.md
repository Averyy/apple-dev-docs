# delegate

**Framework**: AppKit  
**Kind**: property

The delegate of the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var delegate: (any NSCandidateListTouchBarItemDelegate)? { get set }
```

## See Also

- [var client: (any NSView & NSTextInputClient)?](nscandidatelisttouchbaritem/client.md)
  The client object for the candidate list item.
- [protocol NSCandidateListTouchBarItemDelegate](nscandidatelisttouchbaritemdelegate.md)
  A set of methods that a candidate list item delegate uses to enable selection state and list visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/delegate)*