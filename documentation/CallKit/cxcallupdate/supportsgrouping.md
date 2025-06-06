# supportsGrouping

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the call can be grouped with other calls.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var supportsGrouping: Bool { get set }
```

## See Also

- [var localizedCallerName: String?](cxcallupdate/localizedcallername.md)
  The localized name of the caller.
- [var remoteHandle: CXHandle?](cxcallupdate/remotehandle.md)
  The handle for the remote party (for an incoming call, this is the caller; for an outgoing call, this is the callee).
- [var hasVideo: Bool](cxcallupdate/hasvideo.md)
  A Boolean value that indicates whether the call includes video in addition to audio.
- [var supportsUngrouping: Bool](cxcallupdate/supportsungrouping.md)
  A Boolean value that indicates whether the call can be ungrouped from other calls.
- [var supportsHolding: Bool](cxcallupdate/supportsholding.md)
  A Boolean value that indicates whether the call can be placed on hold or removed from hold.
- [var supportsDTMF: Bool](cxcallupdate/supportsdtmf.md)
  A Boolean value that indicates whether the call can send DTMF (dual tone multifrequency) tones via hard pause digits or in-call keypad entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallupdate/supportsgrouping)*