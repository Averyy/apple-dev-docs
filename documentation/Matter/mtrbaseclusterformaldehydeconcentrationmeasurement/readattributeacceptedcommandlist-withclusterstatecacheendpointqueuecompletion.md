# readAttributeAcceptedCommandList(withClusterStateCache:endpoint:queue:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class func readAttributeAcceptedCommandList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> [Any]
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func readAttributeAcceptedCommandList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> [Any]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:))*