# playerViewController(_:shouldPresent:)

**Framework**: AVKit  
**Kind**: method

Asks the delegate whether the player view controller presents a content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, shouldPresent proposal: AVContentProposal) -> Bool
```

## Mentions

- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)

#### Return Value

`true` if the player view controller should propose the content; otherwise `false`.

## Parameters

- `playerViewController`: The player view controller.
- `proposal`: The content proposal to present.

## See Also

- [func playerViewController(AVPlayerViewController, didAccept: AVContentProposal)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:).md)
  Tells the delegate when the user accepts the proposed content.
- [func playerViewController(AVPlayerViewController, didReject: AVContentProposal)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:).md)
  Tells the delegate when the user rejects the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:))*