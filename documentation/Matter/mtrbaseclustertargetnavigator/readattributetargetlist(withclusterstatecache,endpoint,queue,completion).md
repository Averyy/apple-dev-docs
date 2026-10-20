# readAttributeTargetList(withClusterStateCache:endpoint:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

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
class func readAttributeTargetList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable ([Any]?, (any Error)?) -> Void)
```

```swift
class func readAttributeTargetList(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> [Any]
```

```objc
+ (void) readAttributeTargetListWithClusterStateCache:(MTRClusterStateCacheContainer *) clusterStateCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completion:(void (^)(NSArray *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertargetnavigator/readattributetargetlist(withclusterstatecache:endpoint:queue:completion:))*