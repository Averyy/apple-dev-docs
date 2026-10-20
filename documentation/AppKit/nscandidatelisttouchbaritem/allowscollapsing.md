# allowsCollapsing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the item can be collapsed.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var allowsCollapsing: Bool { get set }
```

```objc
@property BOOL allowsCollapsing;
```

#### Discussion

When [`true`](../../Swift/true.md), the candidate list item can be collapsed, [`false`](../../Swift/false.md) otherwise.

The default value is [`true`](../../Swift/true.md).

## See Also

### Handling collapsible behavior
- [var isCollapsed: Bool](./iscollapsed.md)
  A Boolean value that controls the visibility of the candidate list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/allowscollapsing)*