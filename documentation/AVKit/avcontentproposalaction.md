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

- [func dismissContentProposal(for: AVContentProposalAction, animated: Bool, completion: (() -> Void)?)](avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:).md)
  Dismisses the current content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalaction)*