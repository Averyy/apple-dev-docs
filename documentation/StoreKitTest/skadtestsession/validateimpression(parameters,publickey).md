# validateImpression(parameters:publicKey:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Validates an impression for a StoreKit-rendered ad.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func validateImpression(parameters: [String : Any], publicKey: String) throws
```

```objc
- (BOOL) validateImpressionWithParameters:(NSDictionary<NSString *,id> *) parameters publicKey:(NSString *) publicKey error:(NSError **) error;
```

#### Discussion

The cryptographic key pair you use for testing may be a different key pair than you use in production. For testing, use keys from the same key pair when you sign the ad impression and when you call [`validateImpression(parameters:publicKey:)`](./validateimpression%28parameters,publickey%29.md).

For more information about signing ad impressions, see [Signing and providing ads](../../StoreKit/signing-and-providing-ads.md).

## Parameters

- `parameters`: A dictionary containing version-specific key values that associate an app installation with an ad campaign for StoreKit-rendered ads. See [Ad network install-validation keys](../../StoreKit/ad-network-install-validation-keys.md) for the list of required keys.
- `publicKey`: The public key of the elliptic curve cryptographic key pair you used to generate the signature for the ad impression.

## See Also

### Validating impressions
- [func validate(SKAdImpression, publicKey: String) throws](./validate%28_,publickey%29.md)
  Validates an impression for a view-through ad.
- [func validateWebAdImpressionPayload(Data, publicKey: String) throws](./validatewebadimpressionpayload%28_,publickey%29.md)
  Validates an impression for a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/validateimpression(parameters:publickey:))*