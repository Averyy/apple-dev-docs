# readAttributeDefaultNTP(withClusterStateCache:endpoint:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class func readAttributeDefaultNTP(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
class func readAttributeDefaultNTP(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> String
```

```objc
+ (void) readAttributeDefaultNTPWithClusterStateCache:(MTRClusterStateCacheContainer *) clusterStateCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completion:(void (^)(NSString *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/readattributedefaultntp(withclusterstatecache:endpoint:queue:completion:))*