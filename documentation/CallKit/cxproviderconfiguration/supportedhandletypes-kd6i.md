# supportedHandleTypes

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

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

For possible values, see [`CXHandle.HandleType`](../cxhandle/handletype.md).

## See Also

### Configuring Call Capabilities
- [var maximumCallGroups: Int](./maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](./maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportsVideo: Bool](./supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [var includesCallsInRecents: Bool](./includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/supportedhandletypes-kd6i)*