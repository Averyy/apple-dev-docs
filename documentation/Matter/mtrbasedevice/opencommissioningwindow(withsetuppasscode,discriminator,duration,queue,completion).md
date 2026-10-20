# openCommissioningWindow(withSetupPasscode:discriminator:duration:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- tvOS 16.2+
- visionOS 1.0+
- watchOS 9.2+

## Declaration

```swift
func openCommissioningWindow(withSetupPasscode setupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t, completion: @escaping @Sendable (MTRSetupPayload?, (any Error)?) -> Void)
```

```swift
func openCommissioningWindow(withSetupPasscode setupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t) async throws -> MTRSetupPayload
```

```objc
- (void) openCommissioningWindowWithSetupPasscode:(NSNumber *) setupPasscode discriminator:(NSNumber *) discriminator duration:(NSNumber *) duration queue:(dispatch_queue_t) queue completion:(MTRDeviceOpenCommissioningWindowHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/opencommissioningwindow(withsetuppasscode:discriminator:duration:queue:completion:))*