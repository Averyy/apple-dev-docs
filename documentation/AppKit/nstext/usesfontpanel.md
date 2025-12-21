# usesFontPanel

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver uses the Font panel and Font menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesFontPanel: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), the receiver responds to messages from the Font panel and from the Font menu and updates the Font panel with the selection font whenever it changes. If `flag` is [`false`](https://developer.apple.com/documentation/Swift/false) the receiver doesn’t do any of these actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/usesfontpanel)*