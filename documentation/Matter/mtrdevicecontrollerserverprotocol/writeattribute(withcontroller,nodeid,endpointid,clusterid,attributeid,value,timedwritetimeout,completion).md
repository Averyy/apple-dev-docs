# writeAttribute(withController:nodeId:endpointId:clusterId:attributeId:value:timedWriteTimeout:completion:)

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
func writeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?, completion: @escaping @Sendable (Any?, (any Error)?) -> Void)
```

```swift
func writeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?) async throws -> Any
```

```objc
- (void) writeAttributeWithController:(id) controller nodeId:(uint64_t) nodeId endpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId attributeId:(NSNumber *) attributeId value:(id) value timedWriteTimeout:(NSNumber *) timeoutMs completion:(MTRValuesHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/writeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:value:timedwritetimeout:completion:))*