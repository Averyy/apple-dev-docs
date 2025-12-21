# supportsVideo

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the provider supports video in addition to audio.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var supportsVideo: Bool { get set }
```

#### Discussion

By default, this property is set to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var maximumCallGroups: Int](cxproviderconfiguration/maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](cxproviderconfiguration/maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](cxproviderconfiguration/supportedhandletypes-kd6i.md)
  The supported handle types.
- [var includesCallsInRecents: Bool](cxproviderconfiguration/includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/supportsvideo)*