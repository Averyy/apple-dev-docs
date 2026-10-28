# dateOfAutomaticAcceptance

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The date that the system automatically accepts a proposal if the user doesn’t intervene.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var dateOfAutomaticAcceptance: Date? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSDate * dateOfAutomaticAcceptance;
```

## Discussion

The system schedules the proposal when you present it, and may unschedule it if the user cancels automatic acceptance, manually accepts, or otherwise dismisses the proposal.

Set this property to `nil` to cancel automatic acceptance.

## See Also

### Configuring the proposal
- [var contentProposal: AVContentProposal?](./contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](../avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var playerLayoutGuide: UILayoutGuide](./playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](./preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/dateofautomaticacceptance)*