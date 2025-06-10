# writeAttribute(withController:nodeId:endpointId:clusterId:attributeId:value:timedWriteTimeout:completion:)

**Framework**: Matter  
**Kind**: method  
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
func writeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?) async throws -> Any
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber, clusterId: NSNumber, attributeId: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?) async throws -> Any
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/writeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:value:timedwritetimeout:completion:))*