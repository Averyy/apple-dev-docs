# subscribe(withController:nodeId:minInterval:maxInterval:params:shouldCache:completion:)

**Framework**: Matter  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func subscribe(withController controller: Any?, nodeId: UInt64, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, shouldCache: Bool) async throws
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func subscribe(withController controller: Any?, nodeId: UInt64, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, shouldCache: Bool) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/subscribe(withcontroller:nodeid:mininterval:maxinterval:params:shouldcache:completion:))*