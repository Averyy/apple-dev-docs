# maximumCallsPerCallGroup

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of calls per call group.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var maximumCallsPerCallGroup: Int { get set }
```

```objc
@property (nonatomic) NSUInteger maximumCallsPerCallGroup;
```

## Discussion

By default, the maximum number is `5`.

## See Also

### Configuring Call Capabilities
- [var maximumCallGroups: Int](./maximumcallgroups.md)
  The maximum number of call groups.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](./supportedhandletypes-kd6i.md)
  The supported handle types.
- [var supportsVideo: Bool](./supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [var includesCallsInRecents: Bool](./includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.
- [supportedHandleTypes](./supportedhandletypes-995uh.md)
  The supported handle types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/maximumcallspercallgroup)*