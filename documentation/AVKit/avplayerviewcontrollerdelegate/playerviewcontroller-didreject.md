# playerViewController(_:didReject:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the user rejects the proposed content.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didReject proposal: AVContentProposal)
```

## Mentions

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

## Parameters

- `playerViewController`: The player view controller.
- `proposal`: The content proposal.

## See Also

- [func playerViewController(AVPlayerViewController, shouldPresent: AVContentProposal) -> Bool](avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:).md)
  Asks the delegate whether the player view controller presents a content proposal.
- [func playerViewController(AVPlayerViewController, didAccept: AVContentProposal)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:).md)
  Tells the delegate when the user accepts the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:))*