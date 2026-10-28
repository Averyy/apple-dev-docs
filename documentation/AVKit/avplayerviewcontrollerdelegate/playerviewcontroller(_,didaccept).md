# playerViewController(_:didAccept:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user accepts the proposed content.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didAccept proposal: AVContentProposal)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController didAcceptContentProposal:(AVContentProposal *) proposal;
```

## Mentions

- [Presenting content proposals in tvOS](../presenting-content-proposals-in-tvos.md)

## Discussion

Implement this method to replace the player’s current player item with a player item for the proposed content.

## Parameters

- `playerViewController`: The player view controller.
- `proposal`: The content proposal.

## See Also

### Responding to content proposals
- [func playerViewController(AVPlayerViewController, shouldPresent: AVContentProposal) -> Bool](./playerviewcontroller%28_,shouldpresent%29.md)
  Asks the delegate whether the player view controller presents a content proposal.
- [func playerViewController(AVPlayerViewController, didReject: AVContentProposal)](./playerviewcontroller%28_,didreject%29.md)
  Tells the delegate when the user rejects the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:))*