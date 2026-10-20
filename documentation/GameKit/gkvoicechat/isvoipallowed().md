# isVoIPAllowed()

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns whether voice chat is available on the device.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
class func isVoIPAllowed() -> Bool
```

```objc
+ (BOOL) isVoIPAllowed;
```

#### Return Value

[`true`](../../Swift/true.md) if voice chat is available to the game.

#### Discussion

Some countries or phone carriers may restrict the availability of Voice-over-IP (VoIP) services. Before creating a `GKVoiceChat` object, your game should first check to see whether the device supports VoIP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/isvoipallowed())*