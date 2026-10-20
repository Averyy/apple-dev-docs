# isCollapsed

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls the visibility of the candidate list.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var isCollapsed: Bool { get set }
```

```objc
@property (getter=isCollapsed) BOOL collapsed;
```

#### Discussion

When [`true`](../../Swift/true.md), the candidate list is collapsed and not visible to the user.

The default value is [`true`](../../Swift/true.md).

## See Also

### Handling collapsible behavior
- [var allowsCollapsing: Bool](./allowscollapsing.md)
  A Boolean value that specifies whether the item can be collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/iscollapsed)*