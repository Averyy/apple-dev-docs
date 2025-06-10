# verify(_:signature:algorithm:completion:)

**Framework**: Local Authentication  
**Kind**: method

Verifies a digital signature for the data you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func verify(_ signedData: Data, signature: Data, algorithm: SecKeyAlgorithm) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func verify(_ signedData: Data, signature: Data, algorithm: SecKeyAlgorithm) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `signedData`: The signed data.
- `signature`: The signature of the data.
- `algorithm`: An algorithm suitable for verifying signatures with this public key.
- `handler`: A completion handler to call when the verification operation completes.

## See Also

- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](lapublickey/encrypt(_:algorithm:completion:).md)
  Encrypts the data you supply with a given algorithm.
- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](lapublickey/exportbytes(completion:).md)
  Exports the data that represents a public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/verify(_:signature:algorithm:completion:))*