# run(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Runs the user interaction and asynchronously receives a reply.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func run() async throws -> Bool
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func run() async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func run() async throws -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func cancel() -> Bool](tksmartcarduserinteraction/cancel.md)
  Attempts to cancel an interaction started by calling [`run(reply:)`](tksmartcarduserinteraction/run(reply:).md). For certain interactions, cancellation may not be available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/run(reply:))*