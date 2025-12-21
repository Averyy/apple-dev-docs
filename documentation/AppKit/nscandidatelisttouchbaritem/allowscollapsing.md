# allowsCollapsing

**Framework**: AppKit  
**Kind**: property

A Boolean value that specifies whether the item can be collapsed.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var allowsCollapsing: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), the candidate list item can be collapsed, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isCollapsed: Bool](nscandidatelisttouchbaritem/iscollapsed.md)
  A Boolean value that controls the visibility of the candidate list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/allowscollapsing)*