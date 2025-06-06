# SKStoreProductParameterITunesItemIdentifier

**Framework**: StoreKit  
**Kind**: var

The key representing the iTunes identifier for the item you want the store to display when the view controller is presented.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
let SKStoreProductParameterITunesItemIdentifier: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)

#### Discussion

The value for this key, an iTunes item identifier, is an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

To find a product’s iTunes identifier, go to [`linkmaker.itunes.apple.com`](https://developer.apple.comhttp://linkmaker.itunes.apple.com/us/) and search for the product, then locate the iTunes identifier in the link URL. For example, the iTunes identifier for the iBooks app is 364709193.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteritunesitemidentifier)*