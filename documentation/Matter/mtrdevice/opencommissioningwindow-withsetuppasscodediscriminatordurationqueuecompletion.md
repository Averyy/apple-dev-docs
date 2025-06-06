# openCommissioningWindow(withSetupPasscode:discriminator:duration:queue:completion:)

**Framework**: Matter  
**Kind**: method

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
func openCommissioningWindow(withSetupPasscode setupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t) async throws -> MTRSetupPayload
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func openCommissioningWindow(withSetupPasscode setupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t) async throws -> MTRSetupPayload
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func openCommissioningWindow(withSetupPasscode setupPasscode: NSNumber, discriminator: NSNumber, duration: NSNumber, queue: dispatch_queue_t) async throws -> MTRSetupPayload
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/opencommissioningwindow(withsetuppasscode:discriminator:duration:queue:completion:))*