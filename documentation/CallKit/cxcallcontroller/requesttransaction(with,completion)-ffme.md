# requestTransaction(with:completion:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Requests that the transaction that contains the specified action be asynchronously performed by the telephony provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func requestTransaction(with action: CXAction, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func requestTransaction(with action: CXAction) async throws
```

```objc
- (void) requestTransactionWithAction:(CXAction *) action completion:(void (^)(NSError *error)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestTransaction(with action: CXAction) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `action`: The telephony action associated with a call object.
- `completion`: Code to be executed after the transaction is completed. The callback is executed on the queue specified when the call controller was initialized.

  - **transaction**: The requested transaction.
  - **error**: If an error occurred, an error object indicating how the transaction failed, otherwise `nil`.

## See Also

### Requesting Transactions
- [func request(CXTransaction, completion: ((any Error)?) -> Void)](./request%28_,completion%29.md)
  Requests that the actions in the specified transaction be asynchronously performed by the telephony provider.
- [func requestTransaction(with: [CXAction], completion: ((any Error)?) -> Void)](./requesttransaction%28with,completion%29-4o1m4.md)
  Requests that the transaction that contains the specified actions be asynchronously performed by the telephony provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallcontroller/requesttransaction(with:completion:)-ffme)*