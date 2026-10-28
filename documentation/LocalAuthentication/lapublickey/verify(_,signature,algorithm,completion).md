# verify(_:signature:algorithm:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Verifies a digital signature for the data you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func verify(_ signedData: Data, signature: Data, algorithm: SecKeyAlgorithm, completion handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func verify(_ signedData: Data, signature: Data, algorithm: SecKeyAlgorithm) async throws
```

```objc
- (void) verifyData:(NSData *) signedData signature:(NSData *) signature secKeyAlgorithm:(SecKeyAlgorithm) algorithm completion:(void (^)(NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func verify(_ signedData: Data, signature: Data, algorithm: SecKeyAlgorithm) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `signedData`: The signed data.
- `signature`: The signature of the data.
- `algorithm`: An algorithm suitable for verifying signatures with this public key.
- `handler`: A completion handler to call when the verification operation completes.

  - **`error`**: An error object that indicates why the verification operation failed, or `nil` if it succeeded.

## See Also

### Performing cryptographic operations
- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./encrypt%28_,algorithm,completion%29.md)
  Encrypts the data you supply with a given algorithm.
- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](./exportbytes%28completion%29.md)
  Exports the data that represents a public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/verify(_:signature:algorithm:completion:))*