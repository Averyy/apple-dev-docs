# readAttributeProductAppearance(withClusterStateCache:endpoint:queue:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class func readAttributeProductAppearance(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> MTRBasicInformationClusterProductAppearanceStruct
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func readAttributeProductAppearance(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> MTRBasicInformationClusterProductAppearanceStruct
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation/readattributeproductappearance(withclusterstatecache:endpoint:queue:completion:))*