# request(_:completion:)

**Framework**: CallKit  
**Kind**: method

Requests that the actions in the specified transaction be asynchronously performed by the telephony provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func request(_ transaction: CXTransaction) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func request(_ transaction: CXTransaction) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func request(_ transaction: CXTransaction) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `transaction`: A transaction that contains actions to be performed.
- `completion`: Code to be executed after the transaction is completed. The callback is executed on the queue specified when the call controller was initialized.

## See Also

- [func requestTransaction(with: CXAction, completion: ((any Error)?) -> Void)](cxcallcontroller/requesttransaction(with:completion:)-ffme.md)
  Requests that the transaction that contains the specified action be asynchronously performed by the telephony provider.
- [func requestTransaction(with: [CXAction], completion: ((any Error)?) -> Void)](cxcallcontroller/requesttransaction(with:completion:)-4o1m4.md)
  Requests that the transaction that contains the specified actions be asynchronously performed by the telephony provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallcontroller/request(_:completion:))*