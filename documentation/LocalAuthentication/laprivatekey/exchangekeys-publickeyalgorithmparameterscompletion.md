# exchangeKeys(publicKey:algorithm:parameters:completion:)

**Framework**: Local Authentication  
**Kind**: method

Performs a Diffie-Hellman style key exchange operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func exchangeKeys(publicKey: Data, algorithm: SecKeyAlgorithm, parameters: [AnyHashable : Any]) async throws -> Data
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func exchangeKeys(publicKey: Data, algorithm: SecKeyAlgorithm, parameters: [AnyHashable : Any]) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func exchangeKeys(publicKey: Data, algorithm: SecKeyAlgorithm, parameters: [AnyHashable : Any]) async throws -> Data
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The algorithm you use determines the parameters in the dictionary that are required or optional. For more information, see [`SecKeyKeyExchangeParameter`](https://developer.apple.com/documentation/Security/SecKeyKeyExchangeParameter).

## Parameters

- `publicKey`: The remote party’s public key.
- `algorithm`: An algorithm suitable for performing this key exchange. For example,  .
- `parameters`: A dictionary with parameters for this key exchange.
- `handler`: A completion handler to call when the key exchange operation completes.

## See Also

- [func decrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](laprivatekey/decrypt(_:algorithm:completion:).md)
  Decrypts the data you supply with a given algorithm.
- [func sign(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](laprivatekey/sign(_:algorithm:completion:).md)
  Generates a digital signature for the data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey/exchangekeys(publickey:algorithm:parameters:completion:))*