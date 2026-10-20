# shared

**Framework**: DeviceCheck  
**Kind**: property  
**Role**: Type Property

The shared App Attest service that you use to validate your app.

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
class var shared: DCAppAttestService { get }
```

```objc
@property (class, readonly) DCAppAttestService * sharedService;
```

## Mentions

- [Establishing your app’s integrity](../establishing-your-app-s-integrity.md)
- [Validating apps that connect to your server](../validating-apps-that-connect-to-your-server.md)

#### Discussion

Use the shared instance of the service to generate and to certify a cryptographic key, and then to assert your app’s validity using that key.

## See Also

### Accessing the service
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether a particular device provides the App Attest service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcappattestservice/shared)*