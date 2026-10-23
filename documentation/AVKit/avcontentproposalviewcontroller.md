# AVContentProposalViewController

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A view controller that proposes content to watch next.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
class AVContentProposalViewController
```

```objc
@interface AVContentProposalViewController : UIViewController
```

## Mentions

- [Presenting content proposals in tvOS](./presenting-content-proposals-in-tvos.md)

#### Overview

Subclass this class to define the user interface for your content proposal.

## Topics

### Configuring the proposal
- [var contentProposal: AVContentProposal?](./avcontentproposalviewcontroller/contentproposal.md)
  A prosal of content to play.
- [class AVContentProposal](./avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [var dateOfAutomaticAcceptance: Date?](./avcontentproposalviewcontroller/dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](./avcontentproposalviewcontroller/playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](./avcontentproposalviewcontroller/preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.
### Dismissing the proposal
- [func dismissContentProposal(for: AVContentProposalAction, animated: Bool, completion: (() -> Void)?)](./avcontentproposalviewcontroller/dismisscontentproposal%28for,animated,completion%29.md)
  Dismisses the current content proposal.
- [enum AVContentProposalAction](./avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.
### Accessing the player view controller
- [var playerViewController: AVPlayerViewController?](./avcontentproposalviewcontroller/playerviewcontroller.md)
  The player view controller that presents a content proposal.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Content proposals and parental controls
- [Presenting content proposals in tvOS](./presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with overlays and parental controls in tvOS](./working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [class AVContentProposal](./avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [enum AVContentProposalAction](./avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller)*