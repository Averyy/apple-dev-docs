# usesFontPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver uses the Font panel and Font menu.

**Availability**:
- macOS

## Declaration

```swift
var usesFontPanel: Bool { get set }
```

```objc
@property BOOL usesFontPanel;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md), the receiver responds to messages from the Font panel and from the Font menu and updates the Font panel with the selection font whenever it changes. If `flag` is [`false`](../../Swift/false.md) the receiver doesn’t do any of these actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/usesfontpanel)*