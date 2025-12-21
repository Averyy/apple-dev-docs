# invokeCommand(withEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:clientQueue:completion:)

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
func invokeCommand(withEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout timeout: NSNumber?, clientQueue queue: dispatch_queue_t) async throws -> [[String : Any]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/invokecommand(withendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:timedinvoketimeout:clientqueue:completion:))*