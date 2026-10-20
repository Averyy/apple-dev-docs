# deviceController(_:nodeID:getStateWithReply:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func deviceController(_ controller: UUID, nodeID: NSNumber, getStateWithReply reply: @escaping @Sendable (MTRDeviceState) -> Void)
```

```swift
func deviceControllerGetState(_ controller: UUID, nodeID: NSNumber) async -> MTRDeviceState
```

```objc
- (void) deviceController:(NSUUID *) controller nodeID:(NSNumber *) nodeID getStateWithReply:(void (^)(MTRDeviceState state)) reply;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getstatewithreply:))*