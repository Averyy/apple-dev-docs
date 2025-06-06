# contentProposal

**Framework**: AVKit  
**Kind**: property

A prosal of content to play.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
var contentProposal: AVContentProposal? { get }
```

#### Discussion

The associated player view controller sets this property value.

## See Also

- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](avcontentproposalviewcontroller/dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](avcontentproposalviewcontroller/playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](avcontentproposalviewcontroller/preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/contentproposal)*