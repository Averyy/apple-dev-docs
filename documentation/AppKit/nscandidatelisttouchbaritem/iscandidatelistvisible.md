# isCandidateListVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that represents the visibility of this item’s candidate list.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isCandidateListVisible: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), then the candidate list is currently visible, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

When [`isCollapsed`](nscandidatelisttouchbaritem/iscollapsed.md) is [`false`](https://developer.apple.com/documentation/Swift/false), and the item is not obscured by UI then this property is true.

This property is KVO compliant, and you should supply a candidate list when its value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func update(withInsertionPointVisibility: Bool)](nscandidatelisttouchbaritem/update(withinsertionpointvisibility:).md)
  Updates the candidate list visibility configuration based on the client’s insertion point state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/iscandidatelistvisible)*