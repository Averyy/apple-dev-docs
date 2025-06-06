# playerViewController

**Framework**: AVKit  
**Kind**: property

The player view controller that presents a content proposal.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
weak var playerViewController: AVPlayerViewController? { get }
```

#### Discussion

The framework sets this property value during the presentation of the content proposal. It may be `nil` at other times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/playerviewcontroller)*