# validateWebAdImpressionPayload(_:publicKey:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

Validates an impression for a web ad.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
func validateWebAdImpressionPayload(_ impressionData: Data, publicKey: String) throws
```

```objc
- (BOOL) validateWebAdImpressionPayload:(NSData *) impressionData publicKey:(NSString *) publicKey error:(NSError **) error;
```

## See Also

### Validating impressions
- [func validate(SKAdImpression, publicKey: String) throws](./validate%28_,publickey%29.md)
  Validates an impression for a view-through ad.
- [func validateImpression(parameters: [String : Any], publicKey: String) throws](./validateimpression%28parameters,publickey%29.md)
  Validates an impression for a StoreKit-rendered ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/validatewebadimpressionpayload(_:publickey:))*