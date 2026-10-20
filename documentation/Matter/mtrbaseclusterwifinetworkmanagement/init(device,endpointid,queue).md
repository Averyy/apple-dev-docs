# init(device:endpointID:queue:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.

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
init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)
```

```objc
- (instancetype) initWithDevice:(MTRBaseDevice *) device endpointID:(NSNumber *) endpointID queue:(dispatch_queue_t) queue;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwifinetworkmanagement/init(device:endpointid:queue:))*