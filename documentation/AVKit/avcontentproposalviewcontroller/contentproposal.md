# contentProposal

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A prosal of content to play.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var contentProposal: AVContentProposal? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVContentProposal * contentProposal;
```

## Discussion

The associated player view controller sets this property value.

## See Also

### Configuring the proposal
- [class AVContentProposal](../avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](./dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](./playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](./preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/contentproposal)*