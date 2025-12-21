# attestKey(_:clientDataHash:completionHandler:)

**Framework**: DeviceCheck  
**Kind**: method

Asks Apple to attest to the validity of a generated cryptographic key.

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
func attestKey(_ keyId: String, clientDataHash: Data) async throws -> Data
```

## Mentions

- [Attestation Object Validation Guide](attestation-object-validation-guide.md)
- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
- [Preparing to use the app attest service](preparing-to-use-the-app-attest-service.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func attestKey(_ keyId: String, clientDataHash: Data) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method asks Apple to attest to the validity of a key that you previously generated with a call to the [`generateKey(completionHandler:)`](dcappattestservice/generatekey(completionhandler:).md) method. Provide the method with both the key identifier and a computed hash of a data block that includes a one-time challenge from your server to prevent replay attacks. For example, you can use CryptoKit to create a [`SHA256`](https://developer.apple.com/documentation/CryptoKit/SHA256) hash of challenge data:

```swift
import CryptoKit let hash = Data(SHA256.hash(data: challenge)) // A
challenge from your server.
```

The attest method calls its completion handler to return an attestation object to you, which you must send to your server for verification. A compromised version of your app could falsify the verification result, thus circumventing App Attest.

If you successfully verify the attestation object on your server, as described in [`Validating apps that connect to your server`](validating-apps-that-connect-to-your-server.md), then you can associate the key identifier with the user on the device for future reference. You’ll need the identifier to generate assertions with calls to [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md). If your server fails to verify the attestation object, discard the key identifier.

If the method’s completion handler returns the [`serverUnavailable`](dcerror-swift.struct/serverunavailable.md) error — typically due to network connectivity issues — it means that the framework failed to reach the App Attest service to complete the attestation. In this case, retry attestation again using the same key and client data hash later to avoid unnecessarily generating new keys. Retrying with the same inputs helps to preserve the risk metric for a given device.

## Parameters

- `keyId`: The identifier you received when generating a cryptographic key by   calling the    method.
- `clientDataHash`: A SHA256 hash of a unique, single-use data block that   embeds a challenge from your server. Should be at least 16 bytes in length.
- `completionHandler`: A closure that the method calls upon completion with   the following parameters:

## See Also

- [func generateKey(completionHandler: (String?, (any Error)?) -> Void)](dcappattestservice/generatekey(completionhandler:).md)
  Creates a new cryptographic key for use with the App Attest service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice/attestkey(_:clientdatahash:completionhandler:))*