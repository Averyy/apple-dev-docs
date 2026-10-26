# supportsVideo

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL supportsVideo;
```

#### Discussion

By default, this property is set to [`false`](../../Swift/false.md).

## See Also

### Configuring Call Capabilities
- [var maximumCallGroups: Int](./maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](./maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](./supportedhandletypes-kd6i.md)
  The supported handle types.
- [var includesCallsInRecents: Bool](./includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.
- [supportedHandleTypes](./supportedhandletypes-995uh.md)
  The supported handle types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/supportsvideo)*