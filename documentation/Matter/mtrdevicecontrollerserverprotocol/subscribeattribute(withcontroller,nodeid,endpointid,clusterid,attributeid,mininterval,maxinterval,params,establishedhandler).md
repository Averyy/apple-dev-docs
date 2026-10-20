# subscribeAttribute(withController:nodeId:endpointId:clusterId:attributeId:minInterval:maxInterval:params:establishedHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func subscribeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, establishedHandler: @escaping () -> Void)
```

```objc
- (void) subscribeAttributeWithController:(id) controller nodeId:(uint64_t) nodeId endpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId attributeId:(NSNumber *) attributeId minInterval:(NSNumber *) minInterval maxInterval:(NSNumber *) maxInterval params:(NSDictionary<NSString *,id> *) params establishedHandler:(dispatch_block_t) establishedHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/subscribeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:mininterval:maxinterval:params:establishedhandler:))*