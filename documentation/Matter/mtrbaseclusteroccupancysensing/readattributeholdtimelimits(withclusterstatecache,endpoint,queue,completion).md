# readAttributeHoldTimeLimits(withClusterStateCache:endpoint:queue:completion:)

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
class func readAttributeHoldTimeLimits(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable (MTROccupancySensingClusterHoldTimeLimitsStruct?, (any Error)?) -> Void)
```

```swift
class func readAttributeHoldTimeLimits(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> MTROccupancySensingClusterHoldTimeLimitsStruct
```

```objc
+ (void) readAttributeHoldTimeLimitsWithClusterStateCache:(MTRClusterStateCacheContainer *) clusterStateCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completion:(void (^)(MTROccupancySensingClusterHoldTimeLimitsStruct *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroccupancysensing/readattributeholdtimelimits(withclusterstatecache:endpoint:queue:completion:))*