# downloadLog(of:timeout:queue:completion:)

**Framework**: Matter  
**Kind**: method

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
func downloadLog(of type: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t) async throws -> URL
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func downloadLog(of type: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t) async throws -> URL
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func downloadLog(of type: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t) async throws -> URL
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/downloadlog(of:timeout:queue:completion:))*