# remove(_:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func remove(_ endpoint: MTRServerEndpoint, queue: dispatch_queue_t, completion: @escaping @Sendable () -> Void)
```

```swift
func remove(_ endpoint: MTRServerEndpoint, queue: dispatch_queue_t) async
```

```objc
- (void) removeServerEndpoint:(MTRServerEndpoint *) endpoint queue:(dispatch_queue_t) queue completion:(dispatch_block_t) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/remove(_:queue:completion:))*