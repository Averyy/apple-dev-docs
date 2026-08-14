# isVoIPAllowed()

**Framework**: GameKit  
**Kind**: method

Returns whether voice chat is available on the device.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func isVoIPAllowed() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if voice chat is available to the game.

#### Discussion

Some countries or phone carriers may restrict the availability of Voice-over-IP (VoIP) services. Before creating a `GKVoiceChat` object, your game should first check to see whether the device supports VoIP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/isvoipallowed())*