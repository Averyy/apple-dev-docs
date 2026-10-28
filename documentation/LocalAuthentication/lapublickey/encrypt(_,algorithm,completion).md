# encrypt(_:algorithm:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Encrypts the data you supply with a given algorithm.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encrypt(_ data: Data, algorithm: SecKeyAlgorithm, completion handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func encrypt(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
```

```objc
- (void) encryptData:(NSData *) data secKeyAlgorithm:(SecKeyAlgorithm) algorithm completion:(void (^)(NSData *, NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func encrypt(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `data`: The data to encrypt.
- `algorithm`: The algorithm to use to encrypt the data.
- `handler`: A completion handler to call when the encryption operation completes.

  - **`data`**: The encrypted data.
  - **`error`**: An error object that indicates why the encryption failed, or `nil` if it succeeded.

## See Also

### Performing cryptographic operations
- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](./exportbytes%28completion%29.md)
  Exports the data that represents a public key.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](./verify%28_,signature,algorithm,completion%29.md)
  Verifies a digital signature for the data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/encrypt(_:algorithm:completion:))*