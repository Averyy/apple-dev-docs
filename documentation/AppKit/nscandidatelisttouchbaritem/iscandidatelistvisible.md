# isCandidateListVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that represents the visibility of this item’s candidate list.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var isCandidateListVisible: Bool { get }
```

```objc
@property (readonly, getter=isCandidateListVisible) BOOL candidateListVisible;
```

## Discussion

If [`true`](../../Swift/true.md), then the candidate list is currently visible, [`false`](../../Swift/false.md) otherwise.

When [`isCollapsed`](./iscollapsed.md) is [`false`](../../Swift/false.md), and the item is not obscured by UI then this property is true.

This property is KVO compliant, and you should supply a candidate list when its value is [`true`](../../Swift/true.md).

## See Also

### Managing candidate list visibility
- [func update(withInsertionPointVisibility: Bool)](./update%28withinsertionpointvisibility%29.md)
  Updates the candidate list visibility configuration based on the client’s insertion point state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/iscandidatelistvisible)*