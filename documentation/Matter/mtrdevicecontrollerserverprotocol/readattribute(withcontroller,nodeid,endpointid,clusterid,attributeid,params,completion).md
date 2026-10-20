# readAttribute(withController:nodeId:endpointId:clusterId:attributeId:params:completion:)

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
func readAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: [String : Any]?, completion: @escaping @Sendable (Any?, (any Error)?) -> Void)
```

```swift
func readAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: [String : Any]?) async throws -> Any
```

```objc
- (void) readAttributeWithController:(id) controller nodeId:(uint64_t) nodeId endpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId attributeId:(NSNumber *) attributeId params:(NSDictionary<NSString *,id> *) params completion:(MTRValuesHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/readattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:params:completion:))*