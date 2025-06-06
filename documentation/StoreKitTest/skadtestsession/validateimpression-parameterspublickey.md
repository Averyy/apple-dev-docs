# validateImpression(parameters:publicKey:)

**Framework**: StoreKit Test  
**Kind**: method

Validates an impression for a StoreKit-rendered ad.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func validateImpression(parameters: [String : Any], publicKey: String) throws
```

#### Discussion

The cryptographic key pair you use for testing may be a different key pair than you use in production. For testing, use keys from the same key pair when you sign the ad impression and when you call [`validateImpression(parameters:publicKey:)`](skadtestsession/validateimpression(parameters:publickey:).md).

For more information about signing ad impressions, see [`Signing and providing ads`](https://developer.apple.com/documentation/StoreKit/signing-and-providing-ads).

## Parameters

- `parameters`: A dictionary containing version-specific key values that associate an app installation with an ad campaign for StoreKit-rendered ads. See   for the list of required keys.
- `publicKey`: The public key of the elliptic curve cryptographic key pair you used to generate the signature for the ad impression.

## See Also

- [func validate(SKAdImpression, publicKey: String) throws](skadtestsession/validate(_:publickey:).md)
  Validates an impression for a view-through ad.
- [func validateWebAdImpressionPayload(Data, publicKey: String) throws](skadtestsession/validatewebadimpressionpayload(_:publickey:).md)
  Validates an impression for a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/validateimpression(parameters:publickey:))*