# exportBytes(completion:)

**Framework**: Local Authentication  
**Kind**: method

Exports the data that represents a public key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var bytes: Data { get async throws }
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
var bytes: Data { get async throws }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
var bytes: Data { get async throws }
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `handler`: A completion handler to call when the export operation completes.

## See Also

- [func encrypt(Data, algorithm: SecKeyAlgorithm, completion: (Data?, (any Error)?) -> Void)](lapublickey/encrypt(_:algorithm:completion:).md)
  Encrypts the data you supply with a given algorithm.
- [func verify(Data, signature: Data, algorithm: SecKeyAlgorithm, completion: ((any Error)?) -> Void)](lapublickey/verify(_:signature:algorithm:completion:).md)
  Verifies a digital signature for the data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/exportbytes(completion:))*