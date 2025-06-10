# readAttributeGeneratedCommandList(withClusterStateCache:endpoint:queue:completion:)

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
class func readAttributeGeneratedCommandList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> [Any]
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func readAttributeGeneratedCommandList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> [Any]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:))*