# validate(_:publicKey:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Validates an impression for a view-through ad.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func validate(_ impression: SKAdImpression, publicKey: String) throws
```

```objc
- (BOOL) validateImpression:(SKAdImpression *) impression publicKey:(NSString *) publicKey error:(NSError **) error;
```

#### Discussion

The cryptographic key pair you use for testing may be a different key pair than you use in production. For testing, use keys from the same key pair to sign the ad impression for testing and call [`validate(_:publicKey:)`](./validate%28_,publickey%29.md).

For more information about signing ad impressions, see [Signing and providing ads](../../StoreKit/signing-and-providing-ads.md).

## Parameters

- `impression`: An [`SKAdImpression`](../../StoreKit/skadimpression.md) instance, representing your ad impression.
- `publicKey`: The public key of the elliptic curve cryptographic key pair you used to generate the signature for the ad impression.

## See Also

### Validating impressions
- [func validateImpression(parameters: [String : Any], publicKey: String) throws](./validateimpression%28parameters,publickey%29.md)
  Validates an impression for a StoreKit-rendered ad.
- [func validateWebAdImpressionPayload(Data, publicKey: String) throws](./validatewebadimpressionpayload%28_,publickey%29.md)
  Validates an impression for a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/validate(_:publickey:))*