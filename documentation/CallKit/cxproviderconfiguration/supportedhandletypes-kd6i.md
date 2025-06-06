# supportedHandleTypes

**Framework**: CallKit  
**Kind**: property

The supported handle types.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@nonobjc
final var supportedHandleTypes: Set<CXHandle.HandleType> { get set }
```

#### Discussion

For possible values, see [`CXHandle.HandleType`](cxhandle/handletype.md).

## See Also

- [var maximumCallGroups: Int](cxproviderconfiguration/maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](cxproviderconfiguration/maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportsVideo: Bool](cxproviderconfiguration/supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [var includesCallsInRecents: Bool](cxproviderconfiguration/includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/supportedhandletypes-kd6i)*