# remoteHandle

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The handle for the remote party (for an incoming call, this is the caller; for an outgoing call, this is the callee).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var remoteHandle: CXHandle? { get set }
```

```objc
@property (nonatomic, copy, nullable) CXHandle * remoteHandle;
```

## See Also

### Accessing Call Update Attributes
- [var localizedCallerName: String?](./localizedcallername.md)
  The localized name of the caller.
- [var hasVideo: Bool](./hasvideo.md)
  A Boolean value that indicates whether the call includes video in addition to audio.
- [var supportsGrouping: Bool](./supportsgrouping.md)
  A Boolean value that indicates whether the call can be grouped with other calls.
- [var supportsUngrouping: Bool](./supportsungrouping.md)
  A Boolean value that indicates whether the call can be ungrouped from other calls.
- [var supportsHolding: Bool](./supportsholding.md)
  A Boolean value that indicates whether the call can be placed on hold or removed from hold.
- [var supportsDTMF: Bool](./supportsdtmf.md)
  A Boolean value that indicates whether the call can send DTMF (dual tone multifrequency) tones via hard pause digits or in-call keypad entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallupdate/remotehandle)*