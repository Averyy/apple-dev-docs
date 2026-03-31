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

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Overview

Subclass this class to define the user interface for your content proposal.

## Topics

### Configuring the Proposal
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
### Dismissing the Proposal
- [func dismissContentProposal(for: AVContentProposalAction, animated: Bool, completion: (() -> Void)?)](avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:).md)
  Dismisses the current content proposal.
- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.
### Accessing the Player View Controller
- [var playerViewController: AVPlayerViewController?](avcontentproposalviewcontroller/playerviewcontroller.md)
  The player view controller that presents a content proposal.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller)*