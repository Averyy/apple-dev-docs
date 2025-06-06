# init(issuerData:signature:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes and returns a new add-passes view controller with the issuer data, and signature you provide.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(issuerData: Data, signature: Data) throws
```

## Parameters

- `issuerData`: The   object that represents the issuer data.
- `signature`: The   object that represents the issuer’s signature.

## See Also

- [init?(pass: PKPass)](pkaddpassesviewcontroller/init(pass:).md)
  Initializes and returns a newly created add-passes view controller with a single pass.
- [init?(passes: [PKPass])](pkaddpassesviewcontroller/init(passes:).md)
  Initializes and returns a newly created add-passes view controller with an array of passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/init(issuerdata:signature:))*