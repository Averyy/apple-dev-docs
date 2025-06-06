# client

**Framework**: AppKit  
**Kind**: property

The client object for the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var client: (any NSView & NSTextInputClient)? { get set }
```

#### Discussion

This object must be a subclass of [`NSView`](nsview.md) and adopt the [`NSTextInputClient`](nstextinputclient.md) protocol.

The candidate list item uses this property to show completion candidates as users enter text. You can disable this behavior with the [`allowsTextInputContextCandidates`](nscandidatelisttouchbaritem/allowstextinputcontextcandidates.md) property.

## See Also

- [var delegate: (any NSCandidateListTouchBarItemDelegate)?](nscandidatelisttouchbaritem/delegate.md)
  The delegate of the candidate list item.
- [protocol NSCandidateListTouchBarItemDelegate](nscandidatelisttouchbaritemdelegate.md)
  A set of methods that a candidate list item delegate uses to enable selection state and list visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/client)*