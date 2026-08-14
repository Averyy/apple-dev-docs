# includesCallsInRecents

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var includesCallsInRecents: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var maximumCallGroups: Int](cxproviderconfiguration/maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](cxproviderconfiguration/maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](cxproviderconfiguration/supportedhandletypes-kd6i.md)
  The supported handle types.
- [var supportsVideo: Bool](cxproviderconfiguration/supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/includescallsinrecents)*