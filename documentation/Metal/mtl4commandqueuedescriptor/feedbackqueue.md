# feedbackQueue

**Framework**: Metal  
**Kind**: property

Assigns a dispatch queue to which Metal submits feedback notification blocks.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
unowned(unsafe) var feedbackQueue: dispatch_queue_t? { get set }
```

#### Discussion

When you assign a dispatch queue via this method, Metal requires that the queue parameter you provide is a serial queue.

If you set the value of property to `nil`, the default, Metal allocates an internal dispatch queue to service feedback notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueuedescriptor/feedbackqueue)*