# save(completion:)

**Framework**: ClassKit  
**Kind**: method

Saves any changes you’ve made in the data store.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func save() async throws
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func save() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  ClassKit calls your completion handler on an arbitrary thread. If you need to do work on a particular thread from inside the handler, dispatch that work to the appropriate queue.

## Parameters

- `completion`: A closure the method calls on completion of the save operation with an optional error value that indicates the reason for failure, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/save(completion:))*