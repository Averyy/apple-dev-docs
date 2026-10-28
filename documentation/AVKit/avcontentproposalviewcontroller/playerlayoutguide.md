# playerLayoutGuide

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A layout guide that tracks the size and location of the player view.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var playerLayoutGuide: UILayoutGuide { get }
```

```objc
@property (nonatomic, readonly) UILayoutGuide * playerLayoutGuide;
```

## Mentions

- [Presenting content proposals in tvOS](../presenting-content-proposals-in-tvos.md)

## Discussion

The view controller can constrain its views using the anchors of the player layout guide, which has the same size and position as the player view. The layout guide is always relative to the current [`preferredPlayerViewFrame`](./preferredplayerviewframe.md) property value.

## See Also

### Configuring the proposal
- [var contentProposal: AVContentProposal?](./contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](../avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](./dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var preferredPlayerViewFrame: CGRect](./preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/playerlayoutguide)*