# openCommissioningWindow(withDiscriminator:duration:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func openCommissioningWindow(withDiscriminator discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable (MTRSetupPayload?, (any Error)?) -> Void)
```

```swift
func openCommissioningWindow(withDiscriminator discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t) async throws -> MTRSetupPayload
```

```objc
- (void) openCommissioningWindowWithDiscriminator:(NSNumber *) discriminator duration:(NSNumber *) duration queue:(dispatch_queue_t) queue completion:(MTRDeviceOpenCommissioningWindowHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/opencommissioningwindow(withdiscriminator:duration:queue:completion:))*