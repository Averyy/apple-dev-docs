# generateKey(completionHandler:)

**Framework**: DeviceCheck  
**Kind**: method

Creates a new cryptographic key for use with the App Attest service.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func generateKey() async throws -> String
```

## Mentions

- [Attestation Object Validation Guide](attestation-object-validation-guide.md)
- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func generateKey() async throws -> String
``` For example: ```swift
let keyIdentifier = try await generateKey()
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Call this method to request the creation of a secure, unattested key pair on a device for a specific user. On success, the method provides your app with an identifier that represents the key pair stored in the Secure Enclave. Because there’s no way to use or retrieve the key without the identifier, you’ll want to either record it in your app or on your server right away. If key generation fails, the closure provides a [`DCError`](dcerror-swift.struct.md) that indicates the reason for the failure.

Create a unique key for each user account on a device. Otherwise it’s hard to detect an attack that uses a single compromised device to serve multiple remote users running a compromised version of your app. For more information, see [`Assessing fraud risk`](assessing-fraud-risk.md).

After you get the identifier, you call the [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) method with the key identifier to ask Apple to attest to the validity of the associated key. Later, you call the [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md) method with the key identifier to answer a challenge from your server, and establish the legitimacy of this instance of your app.

## Parameters

- `completionHandler`: A closure that the method calls upon completion with   the following parameters:

## See Also

- [func attestKey(String, clientDataHash: Data, completionHandler: (Data?, (any Error)?) -> Void)](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md)
  Asks Apple to attest to the validity of a generated cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice/generatekey(completionhandler:))*