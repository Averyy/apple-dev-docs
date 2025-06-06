# localizedCallerName

**Framework**: CallKit  
**Kind**: property

The localized name of the caller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var localizedCallerName: String? { get set }
```

#### Discussion

By default, the system automatically provides a localized caller name using information like the user’s contacts based on the supplied caller identifier. You can set this property to override the system-provided value.

## See Also

- [var remoteHandle: CXHandle?](cxcallupdate/remotehandle.md)
  The handle for the remote party (for an incoming call, this is the caller; for an outgoing call, this is the callee).
- [var hasVideo: Bool](cxcallupdate/hasvideo.md)
  A Boolean value that indicates whether the call includes video in addition to audio.
- [var supportsGrouping: Bool](cxcallupdate/supportsgrouping.md)
  A Boolean value that indicates whether the call can be grouped with other calls.
- [var supportsUngrouping: Bool](cxcallupdate/supportsungrouping.md)
  A Boolean value that indicates whether the call can be ungrouped from other calls.
- [var supportsHolding: Bool](cxcallupdate/supportsholding.md)
  A Boolean value that indicates whether the call can be placed on hold or removed from hold.
- [var supportsDTMF: Bool](cxcallupdate/supportsdtmf.md)
  A Boolean value that indicates whether the call can send DTMF (dual tone multifrequency) tones via hard pause digits or in-call keypad entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallupdate/localizedcallername)*