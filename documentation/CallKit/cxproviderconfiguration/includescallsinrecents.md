# includesCallsInRecents

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL includesCallsInRecents;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring Call Capabilities
- [var maximumCallGroups: Int](./maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](./maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](./supportedhandletypes-kd6i.md)
  The supported handle types.
- [var supportsVideo: Bool](./supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [supportedHandleTypes](./supportedhandletypes-995uh.md)
  The supported handle types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/includescallsinrecents)*