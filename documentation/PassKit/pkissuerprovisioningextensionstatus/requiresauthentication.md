# requiresAuthentication

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether adding a card requires an authorization-user-interface extension provided by your app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var requiresAuthentication: Bool { get set }
```

#### Discussion

If you return `true` your app must provide a [`PKIssuerProvisioningExtensionAuthorizationProviding`](pkissuerprovisioningextensionauthorizationproviding.md) UI extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionstatus/requiresauthentication)*