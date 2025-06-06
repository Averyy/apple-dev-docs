# generateAssertion(_:clientDataHash:completionHandler:)

**Framework**: DeviceCheck  
**Kind**: method

Creates a block of data that demonstrates the legitimacy of an instance of your app running on a device.

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
func generateAssertion(_ keyId: String, clientDataHash: Data) async throws -> Data
```

## Mentions

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func generateAssertion(_ keyId: String, clientDataHash: Data) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func generateAssertion(_ keyId: String, clientDataHash: Data) async throws -> Data
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

After generating a key with the [`generateKey(completionHandler:)`](dcappattestservice/generatekey(completionhandler:).md) method and validating it with the [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) method, you can use the key at critical moments in your app’s life cycle — like when a user tries to access premium content — to reaffirm the legitimacy of a given instance of your app. Do this by using the [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md) method to sign server requests with your attested key.

You provide the key identifier and a hash of the request that includes a challenge from your server to prevent replay attacks, where an attacker reuses captured network traffic to pose as someone else. The method returns an assertion object in its completion handler that you send to your server for verification, as described in [`Establishing your app’s integrity`](establishing-your-app-s-integrity.md).

## Parameters

- `keyId`: The identifier you received when generating a cryptographic key by   calling the    method.
- `clientDataHash`: A SHA256 hash of a unique, single-use data block that   represents the client data to be signed with the attested private key. Should be at least 16 bytes in length.
- `completionHandler`: A closure that the method calls upon completion with   the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice/generateassertion(_:clientdatahash:completionhandler:))*