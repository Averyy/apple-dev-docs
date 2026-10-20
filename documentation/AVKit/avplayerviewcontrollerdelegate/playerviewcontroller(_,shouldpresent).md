# playerViewController(_:shouldPresent:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the player view controller presents a content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, shouldPresent proposal: AVContentProposal) -> Bool
```

```objc
- (BOOL) playerViewController:(AVPlayerViewController *) playerViewController shouldPresentContentProposal:(AVContentProposal *) proposal;
```

## Mentions

- [Presenting content proposals in tvOS](../presenting-content-proposals-in-tvos.md)

#### Return Value

`true` if the player view controller should propose the content; otherwise `false`.

## Parameters

- `playerViewController`: The player view controller.
- `proposal`: The content proposal to present.

## See Also

### Responding to content proposals
- [func playerViewController(AVPlayerViewController, didAccept: AVContentProposal)](./playerviewcontroller%28_,didaccept%29.md)
  Tells the delegate when the user accepts the proposed content.
- [func playerViewController(AVPlayerViewController, didReject: AVContentProposal)](./playerviewcontroller%28_,didreject%29.md)
  Tells the delegate when the user rejects the proposed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:))*