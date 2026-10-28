# preferredPlayerViewFrame

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The preferred presentation frame of the player view while the content proposal is active.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var preferredPlayerViewFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect preferredPlayerViewFrame;
```

## Mentions

- [Presenting content proposals in tvOS](../presenting-content-proposals-in-tvos.md)

## Discussion

This value defaults to a rectangle that represents the entire screen bounds, but custom view controllers may return a smaller rectangle, or [`zero`](../../CoreFoundation/cgrect/zero.md) to hide the player view completely. If you return a rectangle smaller that the full-screen bounds, the player view animates its frame to its new size and position.

## See Also

### Configuring the proposal
- [var contentProposal: AVContentProposal?](./contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](../avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](./dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](./playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/preferredplayerviewframe)*