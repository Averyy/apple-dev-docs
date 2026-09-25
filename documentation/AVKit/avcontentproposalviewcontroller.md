# AVContentProposalViewController

**Framework**: AVKit  
**Kind**: class

A view controller that proposes content to watch next.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
class AVContentProposalViewController
```

## Mentions

- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Overview

Subclass this class to define the user interface for your content proposal.

## Topics

### Configuring the proposal
- [var contentProposal: AVContentProposal?](avcontentproposalviewcontroller/contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](avcontentproposalviewcontroller/dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](avcontentproposalviewcontroller/playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](avcontentproposalviewcontroller/preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.
### Dismissing the proposal
- [func dismissContentProposal(for: AVContentProposalAction, animated: Bool, completion: (() -> Void)?)](avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:).md)
  Dismisses the current content proposal.
- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.
### Accessing the player view controller
- [var playerViewController: AVPlayerViewController?](avcontentproposalviewcontroller/playerviewcontroller.md)
  The player view controller that presents a content proposal.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with overlays and parental controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller)*