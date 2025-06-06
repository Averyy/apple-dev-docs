# requestTransaction(with:completion:)

**Framework**: CallKit  
**Kind**: method

Requests that the transaction that contains the specified actions be asynchronously performed by the telephony provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func requestTransaction(with actions: [CXAction]) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestTransaction(with actions: [CXAction]) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func requestTransaction(with actions: [CXAction]) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `actions`: The telephony actions.
- `completion`: Code to be executed after the transaction is completed. The callback is executed on the queue specified when the call controller was initialized.

## See Also

- [func request(CXTransaction, completion: ((any Error)?) -> Void)](cxcallcontroller/request(_:completion:).md)
  Requests that the actions in the specified transaction be asynchronously performed by the telephony provider.
- [func requestTransaction(with: CXAction, completion: ((any Error)?) -> Void)](cxcallcontroller/requesttransaction(with:completion:)-ffme.md)
  Requests that the transaction that contains the specified action be asynchronously performed by the telephony provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallcontroller/requesttransaction(with:completion:)-4o1m4)*