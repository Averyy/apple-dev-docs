# invokeCommand(withEndpointId:clusterId:commandId:commandFields:timedInvokeTimeout:clientQueue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use invokeCommandWithEndpointID:clusterID:commandID:commandFields:timedInvokeTimeout:queue:completion

## Declaration

```swift
func invokeCommand(withEndpointId endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, commandFields: Any, timedInvokeTimeout timeoutMs: NSNumber?, clientQueue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func invokeCommand(withEndpointId endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, commandFields: Any, timedInvokeTimeout timeoutMs: NSNumber?, clientQueue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) invokeCommandWithEndpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId commandId:(NSNumber *) commandId commandFields:(id) commandFields timedInvokeTimeout:(NSNumber *) timeoutMs clientQueue:(dispatch_queue_t) clientQueue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/invokecommand(withendpointid:clusterid:commandid:commandfields:timedinvoketimeout:clientqueue:completion:))*