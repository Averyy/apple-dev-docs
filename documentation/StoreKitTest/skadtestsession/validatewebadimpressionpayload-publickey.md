# validateWebAdImpressionPayload(_:publicKey:)

**Framework**: StoreKit Test  
**Kind**: method

Validates an impression for a web ad.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
func validateWebAdImpressionPayload(_ impressionData: Data, publicKey: String) throws
```

## See Also

- [func validate(SKAdImpression, publicKey: String) throws](skadtestsession/validate(_:publickey:).md)
  Validates an impression for a view-through ad.
- [func validateImpression(parameters: [String : Any], publicKey: String) throws](skadtestsession/validateimpression(parameters:publickey:).md)
  Validates an impression for a StoreKit-rendered ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/validatewebadimpressionpayload(_:publickey:))*