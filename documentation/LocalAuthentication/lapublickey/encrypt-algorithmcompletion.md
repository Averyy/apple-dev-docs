# encrypt(_:algorithm:completion:)

**Framework**: Local Authentication  
**Kind**: method

Encrypts the data you supply with a given algorithm.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encrypt(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func encrypt(_ data: Data, algorithm: SecKeyAlgorithm) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `data`: The data to encrypt.
- `algorithm`: The algorithm to use to encrypt the data.
- `handler`: A completion handler to call when the encryption operation completes.

## See Also

- [func exportBytes(completion: (Data?, (any Error)?) -> Void)](lapublickey/exportbytes(completion:).md)
  Exports the data that represents a public key.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](lapublickey/verify(_:signature:algorithm:completion:).md)
  Verifies a digital signature for the data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/encrypt(_:algorithm:completion:))*