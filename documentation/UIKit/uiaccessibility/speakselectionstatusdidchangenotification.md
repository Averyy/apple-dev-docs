# speakSelectionStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that UIKit posts when the system’s Speak Selection setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let speakSelectionStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

- [static let monoAudioStatusDidChangeNotification: NSNotification.Name](uiaccessibility/monoaudiostatusdidchangenotification.md)
  A notification that UIKit posts when system audio changes from stereo to mono.
- [static let speakScreenStatusDidChangeNotification: NSNotification.Name](uiaccessibility/speakscreenstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Screen setting changes.
- [static let hearingDevicePairedEarDidChangeNotification: NSNotification.Name](uiaccessibility/hearingdevicepairedeardidchangenotification.md)
  A notification that UIKit posts when there’s a change to the currently paired hearing devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/speakselectionstatusdidchangenotification)*