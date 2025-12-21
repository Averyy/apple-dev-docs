# invokeCommand(withEndpointID:clusterID:commandID:commandFields:timedInvokeTimeout:queue:completion:)

**Framework**: Matter  
**Kind**: method

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
func invokeCommand(withEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, timedInvokeTimeout timeoutMs: NSNumber?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/invokecommand(withendpointid:clusterid:commandid:commandfields:timedinvoketimeout:queue:completion:))*