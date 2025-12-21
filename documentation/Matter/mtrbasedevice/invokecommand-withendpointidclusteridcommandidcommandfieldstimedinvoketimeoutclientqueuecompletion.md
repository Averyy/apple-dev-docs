# invokeCommand(withEndpointId:clusterId:commandId:commandFields:timedInvokeTimeout:clientQueue:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
func invokeCommand(withEndpointId endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber, commandFields: Any, timedInvokeTimeout timeoutMs: NSNumber?, clientQueue: dispatch_queue_t) async throws -> [[String : Any]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/invokecommand(withendpointid:clusterid:commandid:commandfields:timedinvoketimeout:clientqueue:completion:))*