# activeChannelUUID

**Framework**: Push to Talk  
**Kind**: property

The unique identifier of the active channel for the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var activeChannelUUID: UUID? { get }
```

#### Discussion

You can activate only one channel at a time. A `nil` value indicates there isn’t an active Push to Talk channel. When this value isn’t `nil`, the channel is active in the user interface, and the ephemeral push token is usable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/activechanneluuid)*