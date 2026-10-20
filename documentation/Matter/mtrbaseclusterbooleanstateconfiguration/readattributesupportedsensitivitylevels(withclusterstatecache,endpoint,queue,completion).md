# readAttributeSupportedSensitivityLevels(withClusterStateCache:endpoint:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

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
class func readAttributeSupportedSensitivityLevels(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
class func readAttributeSupportedSensitivityLevels(withClusterStateCache clusterStateCacheContainer: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> NSNumber
```

```objc
+ (void) readAttributeSupportedSensitivityLevelsWithClusterStateCache:(MTRClusterStateCacheContainer *) clusterStateCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completion:(void (^)(NSNumber *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels(withclusterstatecache:endpoint:queue:completion:))*