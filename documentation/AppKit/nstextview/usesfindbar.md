# usesFindBar

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether to use the find bar for this text view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var usesFindBar: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the find bar is used for this text view; otherwise [`false`](https://developer.apple.com/documentation/Swift/false). See [`NSTextFinder`](nstextfinder.md) for information about the find bar.

A text view can use either a find panel or a find bar. If [`usesFindBar`](nstextview/usesfindbar.md) is set to [`true`](https://developer.apple.com/documentation/Swift/true),  [`usesFindPanel`](nstextview/usesfindpanel.md) is set to [`false`](https://developer.apple.com/documentation/Swift/false) and vice versa.

## See Also

- [var usesFindPanel: Bool](nstextview/usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
- [var isIncrementalSearchingEnabled: Bool](nstextview/isincrementalsearchingenabled.md)
  A Boolean value that indicates whether incremental searching is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfindbar)*