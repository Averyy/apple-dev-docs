# maximumCallGroups

**Framework**: CallKit  
**Kind**: property

The maximum number of call groups.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var maximumCallGroups: Int { get set }
```

#### Discussion

By default, the maximum number is `2`.

## See Also

- [var maximumCallsPerCallGroup: Int](cxproviderconfiguration/maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](cxproviderconfiguration/supportedhandletypes-kd6i.md)
  The supported handle types.
- [var supportsVideo: Bool](cxproviderconfiguration/supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [var includesCallsInRecents: Bool](cxproviderconfiguration/includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/maximumcallgroups)*