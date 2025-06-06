# preferredPlayerViewFrame

**Framework**: AVKit  
**Kind**: property

The preferred presentation frame of the player view while the content proposal is active.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
var preferredPlayerViewFrame: CGRect { get }
```

## Mentions

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Discussion

This value defaults to a rectangle that represents the entire screen bounds, but custom view controllers may return a smaller rectangle, or [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGRect/zero) to hide the player view completely. If you return a rectangle smaller that the full-screen bounds, the player view animates its frame to its new size and position.

## See Also

- [var contentProposal: AVContentProposal?](avcontentproposalviewcontroller/contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](avcontentproposalviewcontroller/dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](avcontentproposalviewcontroller/playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/preferredplayerviewframe)*