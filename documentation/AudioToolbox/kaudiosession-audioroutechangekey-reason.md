# kAudioSession_AudioRouteChangeKey_Reason

**Framework**: Audio Toolbox  
**Kind**: var

Identifies the reason for the audio route change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSession_AudioRouteChangeKey_Reason: String { get }
```

#### Discussion

Value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object that identifies the reason for the audio route change. See [`Audio Route Change Reasons`](1618380-audio-route-change-reasons.md).

#### Discussion

> **Note**:  It is typically more convenient to instead use the [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) version of this constant, [`kAudioSession_RouteChangeKey_Reason`](kaudiosession_routechangekey_reason.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_reason)*