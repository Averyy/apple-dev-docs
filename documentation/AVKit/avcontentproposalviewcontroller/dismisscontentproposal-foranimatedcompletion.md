# dismissContentProposal(for:animated:completion:)

**Framework**: AVKit  
**Kind**: method

Dismisses the current content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
func dismissContentProposal(for action: AVContentProposalAction, animated: Bool) async
```

## Mentions

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func dismissContentProposal(for action: AVContentProposalAction, animated: Bool) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func dismissContentProposal(for action: AVContentProposalAction, animated: Bool) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Call this method to indicate the user action when leaving this proposal.

## Parameters

- `action`: A content proposal action that indicates whether the user accepted, rejected, or deferred the content proposal.
- `animated`: A Boolean value that indicates whether the content proposal dismisses in an animated manner.
- `block`: An optional callback that the system calls when its hidden the conten proposal.

## See Also

- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:))*