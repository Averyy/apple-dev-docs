# Combining parameters to generate a signature for SKAdNetwork 2

**Framework**: StoreKit

Generate signatures to sign your ad with version 2.

#### Overview

To generate the signature, first combine the values of [`Ad network install-validation keys`](ad-network-install-validation-keys.md) for the version 2.

> ❗ **Important**:  Lowercase the string representation of the nonce: [`SKStoreProductParameterAdNetworkNonce`](skstoreproductparameteradnetworknonce.md). Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

 Lowercase the string representation of the nonce: [`SKStoreProductParameterAdNetworkNonce`](skstoreproductparameteradnetworknonce.md). Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

Strings for version 2 and earlier don’t include a `fidelity-type` parameter. For version 2, combine the values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order shown:

Listing 1. Parameter values combined, in order, for version 2.

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + timestamp

```

## See Also

- [Combining parameters to generate signatures for SKAdNetwork 2.2 and 3](combining-parameters-to-generate-signatures-for-skadnetwork-2-2-and-3.md)
  Generate signatures to sign your ad with versions 2.2 and 3.
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)
  Generate signatures for apps compiled with earlier SDKs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/combining-parameters-to-generate-a-signature-for-skadnetwork-2)*