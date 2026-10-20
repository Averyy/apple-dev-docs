# init(device:endpointID:queue:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

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
init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)
```

```objc
- (instancetype) initWithDevice:(MTRBaseDevice *) device endpointID:(NSNumber *) endpointID queue:(dispatch_queue_t) queue;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternetworkcommissioning/init(device:endpointid:queue:))*