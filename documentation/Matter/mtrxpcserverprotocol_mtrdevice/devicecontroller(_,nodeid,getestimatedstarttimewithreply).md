# deviceController(_:nodeID:getEstimatedStartTimeWithReply:)

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
func deviceController(_ controller: UUID, nodeID: NSNumber, getEstimatedStartTimeWithReply reply: @escaping @Sendable (Date?) -> Void)
```

```swift
func deviceControllerGetEstimatedStartTime(_ controller: UUID, nodeID: NSNumber) async -> Date?
```

```objc
- (void) deviceController:(NSUUID *) controller nodeID:(NSNumber *) nodeID getEstimatedStartTimeWithReply:(void (^)(NSDate *estimatedStartTime)) reply;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:getestimatedstarttimewithreply:))*