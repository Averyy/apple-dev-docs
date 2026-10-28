# exportBytes(completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Exports the data that represents a public key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func exportBytes(completion handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
var bytes: Data { get async throws }
```

```objc
- (void) exportBytesWithCompletion:(void (^)(NSData *, NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> var bytes: Data { get async throws }
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `handler`: A completion handler to call when the export operation completes.

  - **`data`**: The data that represents the public key.
  - **`error`**: An error object that indicates why the export operation failed, or `nil` if it succeeded.

## See Also

### Performing cryptographic operations
- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./encrypt%28_,algorithm,completion%29.md)
  Encrypts the data you supply with a given algorithm.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](./verify%28_,signature,algorithm,completion%29.md)
  Verifies a digital signature for the data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/exportbytes(completion:))*