# right(forIdentifier:completion:)

**Framework**: Local Authentication  
**Kind**: method

Fetches a previously stored right from the shared right store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func right(forIdentifier identifier: String) async throws -> LAPersistedRight
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func right(forIdentifier identifier: String) async throws -> LAPersistedRight
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func right(forIdentifier identifier: String) async throws -> LAPersistedRight
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `identifier`: The unique identifier of the right.
- `handler`: A completion handler to call when the right access completes.

## See Also

- [class var shared: LARightStore](larightstore/shared.md)
  A shared object that stores rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore/right(foridentifier:completion:))*