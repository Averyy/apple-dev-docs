# DCAppAttestService

**Framework**: DeviceCheck  
**Kind**: class

A service that you use to validate the instance of your app running on a device.

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
class DCAppAttestService
```

## Mentions

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
- [Validating apps that connect to your server](validating-apps-that-connect-to-your-server.md)

#### Overview

Use the [`shared`](dcappattestservice/shared.md) instance of the [`DCAppAttestService`](dcappattestservice.md) class to assert the legitimacy of a particular instance of your app to your server. After ensuring service availability by reading the [`isSupported`](dcappattestservice/issupported.md) property, you use the service to:

- Create a cryptographic key in the Secure Enclave by calling the [`generateKey(completionHandler:)`](dcappattestservice/generatekey(completionhandler:).md) method.
- Ask Apple to certify the key by calling the [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) method. - Prepare an assertion of your app’s integrity to accompany any or all server requests using the [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md) method.

For more information about how to support App Attest in your app, see [`Establishing your app’s integrity`](establishing-your-app-s-integrity.md). For information about the complementary procedures you implement on your server, see [`Validating apps that connect to your server`](validating-apps-that-connect-to-your-server.md).

> **Note**: To use the App Attest service, your app must have an app ID that you register on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) website.

To use the App Attest service, your app must have an app ID that you register on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) website.

## Topics

### Accessing the service
- [class var shared: DCAppAttestService](dcappattestservice/shared.md)
  The shared App Attest service that you use to validate your app.
- [var isSupported: Bool](dcappattestservice/issupported.md)
  A Boolean value that indicates whether a particular device provides the App Attest service.
### Preparing a key
- [func generateKey(completionHandler: (String?, (any Error)?) -> Void)](dcappattestservice/generatekey(completionhandler:).md)
  Creates a new cryptographic key for use with the App Attest service.
- [func attestKey(String, clientDataHash: Data, completionHandler: (Data?, (any Error)?) -> Void)](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md)
  Asks Apple to attest to the validity of a generated cryptographic key.
### Validating the app instance
- [func generateAssertion(String, clientDataHash: Data, completionHandler: (Data?, (any Error)?) -> Void)](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md)
  Creates a block of data that demonstrates the legitimacy of an instance of your app running on a device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
  Ensure that requests your server receives come from legitimate instances of your app.
- [Validating apps that connect to your server](validating-apps-that-connect-to-your-server.md)
  Verify that connections to your server come from legitimate instances of your app.
- [Assessing fraud risk](assessing-fraud-risk.md)
  Request and analyze risk data using server-to-server calls.
- [Preparing to use the app attest service](preparing-to-use-the-app-attest-service.md)
  Test your implementation in a development environment and onboard users gradually.
- [App Attest Environment](../BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice)*