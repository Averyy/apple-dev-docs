# readAttributes(withEndpointID:clusterID:attributeID:params:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func readAttributes(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, attributeID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func readAttributes(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, attributeID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) readAttributesWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID attributeID:(NSNumber *) attributeID params:(MTRReadParams *) params queue:(dispatch_queue_t) queue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/readattributes(withendpointid:clusterid:attributeid:params:queue:completion:))*