# init(device:endpointID:queue:)

**Framework**: Matter  
**Kind**: init

For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.

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
init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercontentappobserver/init(device:endpointid:queue:))*