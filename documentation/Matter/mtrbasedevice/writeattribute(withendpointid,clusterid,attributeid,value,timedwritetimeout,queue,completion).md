# writeAttribute(withEndpointID:clusterID:attributeID:value:timedWriteTimeout:queue:completion:)

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
func writeAttribute(withEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?, queue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func writeAttribute(withEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, timedWriteTimeout timeoutMs: NSNumber?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) writeAttributeWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID attributeID:(NSNumber *) attributeID value:(id) value timedWriteTimeout:(NSNumber *) timeoutMs queue:(dispatch_queue_t) queue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/writeattribute(withendpointid:clusterid:attributeid:value:timedwritetimeout:queue:completion:))*