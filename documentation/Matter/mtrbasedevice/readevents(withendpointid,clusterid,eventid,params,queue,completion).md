# readEvents(withEndpointID:clusterID:eventID:params:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func readEvents(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, eventID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func readEvents(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, eventID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) readEventsWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID eventID:(NSNumber *) eventID params:(MTRReadParams *) params queue:(dispatch_queue_t) queue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/readevents(withendpointid:clusterid:eventid:params:queue:completion:))*