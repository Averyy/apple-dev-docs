# kAudioSession_AudioRouteChangeKey_Reason

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

Identifies the reason for the audio route change.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
var kAudioSession_AudioRouteChangeKey_Reason: String { get }
```

```c
#define kAudioSession_AudioRouteChangeKey_Reason
```

## Discussion

Value is a [`CFNumber`](../CoreFoundation/cfnumber.md) object that identifies the reason for the audio route change. See [Audio Route Change Reasons](./api-1618380-audio-route-change-reasons.md).

## Discussion

> **Note**:  It is typically more convenient to instead use the [`CFString`](../CoreFoundation/cfstring.md) version of this constant, [`kAudioSession_RouteChangeKey_Reason`](./kaudiosession_routechangekey_reason.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosession_audioroutechangekey_reason)*