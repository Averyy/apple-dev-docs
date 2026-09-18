# AVContentProposalAction

**Framework**: AVKit  
**Kind**: enum

Constant that indicate the action a user takes when dismissing a content proposal.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum AVContentProposalAction
```

## Topics

### Creating an action
- [init?(rawValue: Int)](avcontentproposalaction/init(rawvalue:).md)
### Actions
- [AVContentProposalAction.accept](avcontentproposalaction/accept.md)
  The user accepted the content proposal.
- [AVContentProposalAction.reject](avcontentproposalaction/reject.md)
  The user rejected the content proposal.
- [AVContentProposalAction.defer](avcontentproposalaction/defer.md)
  The user deferred the content proposal.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with overlays and parental controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalaction)*