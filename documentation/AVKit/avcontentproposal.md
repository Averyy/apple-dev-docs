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

- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Overview

A content proposal object models the data about the proposed content such as its title, preview image, presentation time, and content URL. You make a content proposal eligible for presentation by setting it as the [`nextContentProposal`](https://developer.apple.com/documentation/avfoundation/avplayeritem/nextcontentproposal) of the current [`AVPlayerItem`](https://developer.apple.com/documentation/avfoundation/avplayeritem).

```swift
let proposal = AVContentProposal(contentTimeForTransition: time,
                                 title: title,
                                 previewImage: image)
// Set the proposal as the nextContentProposal of the current player item
currentPlayerItem.nextContentProposal = proposal
```

## Topics

### Creating a content proposal
- [init(contentTimeForTransition: CMTime, title: String, previewImage: UIImage?)](avcontentproposal/init(contenttimefortransition:title:previewimage:).md)
  Creates a new content proposal with the specified transition time, title, and preview image.
### Configuring the content proposal
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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with overlays and parental controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal)*