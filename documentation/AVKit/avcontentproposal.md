# AVContentProposal

**Framework**: AVKit  
**Kind**: class

An object that describes the content to propose playing after the current item finishes.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
class AVContentProposal
```

## Mentions

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Overview

A content proposal object models the data about the proposed content such as its title, preview image, presentation time, and content URL. You make a content proposal eligible for presentation by setting it as the [`nextContentProposal`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/nextContentProposal) of the current [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem).

```swift
let proposal = AVContentProposal(contentTimeForTransition: time,
                                 title: title,
                                 previewImage: image)
// Set the proposal as the nextContentProposal of the current player item
currentPlayerItem.nextContentProposal = proposal
```

## Topics

### Creating a Content Proposal
- [init(contentTimeForTransition: CMTime, title: String, previewImage: UIImage?)](avcontentproposal/init(contenttimefortransition:title:previewimage:).md)
  Creates a new content proposal with the specified transition time, title, and preview image.
### Configuring the Content Proposal
- [var contentTimeForTransition: CMTime](avcontentproposal/contenttimefortransition.md)
  The time within the timeline of the current player item when the content proposal presentation should begin.
- [var title: String](avcontentproposal/title.md)
  The title of the proposed content.
- [var previewImage: UIImage?](avcontentproposal/previewimage.md)
  The preview image of the proposed item.
- [var metadata: [AVMetadataItem]](avcontentproposal/metadata.md)
  Optional custom metadata associated with the proposed item.
- [var automaticAcceptanceInterval: TimeInterval](avcontentproposal/automaticacceptanceinterval.md)
  The interval between the time playback ends and automatic acceptance of this content proposal.
- [var url: URL?](avcontentproposal/url.md)
  The URL of the proposed content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var contentProposal: AVContentProposal?](avcontentproposalviewcontroller/contentproposal.md)
  A prosal of content to play.
- [var dateOfAutomaticAcceptance: Date?](avcontentproposalviewcontroller/dateofautomaticacceptance.md)
  The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [var playerLayoutGuide: UILayoutGuide](avcontentproposalviewcontroller/playerlayoutguide.md)
  A layout guide that tracks the size and location of the player view.
- [var preferredPlayerViewFrame: CGRect](avcontentproposalviewcontroller/preferredplayerviewframe.md)
  The preferred presentation frame of the player view while the content proposal is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal)*