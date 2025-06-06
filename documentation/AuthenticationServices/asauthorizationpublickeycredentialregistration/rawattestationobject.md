# rawAttestationObject

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

A data object that contains the returned attestation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var rawAttestationObject: Data? { get }
```

#### Discussion

This object contains the public key. If you request it, it also contains the attestation statement. To learn more, see the [`W3C Web Authentication specification`](https://developer.apple.comhttps://www.w3.org/TR/webauthn-2/#attestation-object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistration/rawattestationobject)*