# sign(_:algorithm:completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Generates a digital signature for the data you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func sign(_ data: Data, algorithm: SecKeyAlgorithm, completion handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func sign(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
```

```objc
- (void) signData:(NSData *) data secKeyAlgorithm:(SecKeyAlgorithm) algorithm completion:(void (^)(NSData *, NSError *)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func sign(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `data`: The data to sign. The data is usually the digest of applying a cryptographic hash function to some actual data.
- `algorithm`: An algorithm suitable for this data signing operation. For example, `ecdsaSignatureMessageX962SHA256`.
- `handler`: A completion handler to call when the signing operation completes.

  - **data**: The signature of the data you supply.
  - **error**: An error object that indicates why the signing operation failed, or `nil` if it succeeded.

## See Also

### Performing cryptographic operations
- [func decrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](./decrypt%28_,algorithm,completion%29.md)
  Decrypts the data you supply with a given algorithm.
- [func exchangeKeys(publicKey: Data, algorithm: SecKeyAlgorithm, parameters: [AnyHashable : Any], completion: (Data?, (any Error)?) -> Void)](./exchangekeys%28publickey,algorithm,parameters,completion%29.md)
  Performs a Diffie-Hellman style key exchange operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey/sign(_:algorithm:completion:))*