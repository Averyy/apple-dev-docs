# invokeCommand(withController:nodeId:endpointId:clusterId:commandId:fields:timedInvokeTimeout:completion:)

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
func invokeCommand(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, fields: Any, timedInvokeTimeout timeoutMs: NSNumber?, completion: @escaping @Sendable (Any?, (any Error)?) -> Void)
```

```swift
func invokeCommand(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, fields: Any, timedInvokeTimeout timeoutMs: NSNumber?) async throws -> Any
```

```objc
- (void) invokeCommandWithController:(id) controller nodeId:(uint64_t) nodeId endpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId commandId:(NSNumber *) commandId fields:(id) fields timedInvokeTimeout:(NSNumber *) timeoutMs completion:(MTRValuesHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/invokecommand(withcontroller:nodeid:endpointid:clusterid:commandid:fields:timedinvoketimeout:completion:))*