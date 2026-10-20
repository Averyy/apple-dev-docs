# localPlayerDidSelect(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when the local player selects a challenge banner displayed by GameKit.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func localPlayerDidSelect(_ challenge: GKChallenge!)
```

```objc
- (void) localPlayerDidSelectChallenge:(GKChallenge *) challenge;
```

## Parameters

- `challenge`: The selected challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/localplayerdidselect(_:))*