# Combining parameters to generate signatures for SKAdNetwork 2.2 and 3

**Framework**: StoreKit

Generate signatures to sign your ad with versions 2.2 and 3.

#### Overview

To generate the signature, combine the required values of [`Ad network install-validation keys`](ad-network-install-validation-keys.md) for version 2, and include a `fidelity-type` value of `1` for StoreKit-rendered ads.

> ❗ **Important**:  Lowercase the string representation of the nonce: [`SKStoreProductParameterAdNetworkNonce`](skstoreproductparameteradnetworknonce.md). Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

For versions 2.2 and 3, combine the values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order the code below shows:

```javascript
//Parameter values combined, in order, for version 2.2 and 3.
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + timestamp

```

## See Also

- [Combining parameters to generate a signature for SKAdNetwork 2](combining-parameters-to-generate-a-signature-for-skadnetwork-2.md)
  Generate signatures to sign your ad with version 2.
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)
  Generate signatures for apps compiled with earlier SDKs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/combining-parameters-to-generate-signatures-for-skadnetwork-2-2-and-3)*