# Combining parameters to generate a signature for SKAdNetwork 1

**Framework**: StoreKit

Generate signatures for apps compiled with earlier SDKs.

#### Overview

Generate a signature using the parameters for version 1.0 if you compile your app with an iOS SDK version from 11.3 through 13.7.

To generate the signature, first combine the values of [`Ad network install-validation keys`](ad-network-install-validation-keys.md) for the version 1.0.

The parameters required for a version 1.0 signature are:

##### Combine the Parameters for Version 10

Create the UTF-8 string for version 1.0 if you compile your app with an SDK prior to iOS 14.

> ❗ **Important**:  You must use lowercase for the string representation of the nonce: [`SKStoreProductParameterAdNetworkNonce`](skstoreproductparameteradnetworknonce.md).

Combine the values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order shown:

```javascript
ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + timestamp

```

Next, follow the instructions to sign the combined string, encode the signature, and use the generated signature string as described in [`Generating the signature to validate StoreKit-rendered ads`](generating-the-signature-to-validate-storekit-rendered-ads.md).

## See Also

- [Combining parameters to generate signatures for SKAdNetwork 2.2 and 3](combining-parameters-to-generate-signatures-for-skadnetwork-2-2-and-3.md)
  Generate signatures to sign your ad with versions 2.2 and 3.
- [Combining parameters to generate a signature for SKAdNetwork 2](combining-parameters-to-generate-a-signature-for-skadnetwork-2.md)
  Generate signatures to sign your ad with version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/combining-parameters-to-generate-a-signature-for-skadnetwork-1)*