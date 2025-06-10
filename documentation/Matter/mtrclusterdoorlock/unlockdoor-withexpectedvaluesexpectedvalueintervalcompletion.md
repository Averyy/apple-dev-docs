# unlockDoor(withExpectedValues:expectedValueInterval:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func unlockDoor(withExpectedValues expectedValues: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func unlockDoor(withExpectedValues expectedValues: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/unlockdoor(withexpectedvalues:expectedvalueinterval:completion:))*