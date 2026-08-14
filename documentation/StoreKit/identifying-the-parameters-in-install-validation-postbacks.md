# Identifying the parameters in install-validation postbacks

**Framework**: StoreKit

Learn about the postback parameters in all SKAdNetwork versions.

#### Overview

The following list describes all the possible parameters you may get in a postback, and their version availability. To verify that Apple signed the postback, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

- **`version`**: Version 2 and later. The SKAdNetwork version that matches [`SKStoreProductParameterAdNetworkVersion`](skstoreproductparameteradnetworkversion.md) or [`version`](skadimpression/version.md). For more information about versions, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md).
- **`ad-network-id`**: Version 1 and later. Your ad network ID, which matches the value you provide for [`SKStoreProductParameterAdNetworkIdentifier`](skstoreproductparameteradnetworkidentifier.md) or [`adNetworkIdentifier`](skadimpression/adnetworkidentifier.md).
- **`attribution-signature`**: Version 2 and later. Apple’s attribution signature that you verify.
- **`app-id`**: Version 1 and later. The App Store app ID of the advertised app.
- **`source-identifier`**: Version 4 and later. The hierarchical source identifier that replaces the `campaign-id`. This string represents two, three, or four digits of the original value the ad network supplies in [`SKStoreProductParameterAdNetworkSourceIdentifier`](skstoreproductparameteradnetworksourceidentifier.md) or [`sourceIdentifier`](skadimpression/sourceidentifier.md).
- **`campaign-id`**: Versions 1–3. The campaign identifer you provide when displaying the ad, which matches [`SKStoreProductParameterAdNetworkCampaignIdentifier`](skstoreproductparameteradnetworkcampaignidentifier.md) or [`adCampaignIdentifier`](skadimpression/adcampaignidentifier.md). Version 4 and later ads use `source-identifer` instead.
- **`source-app-id`**: Version 2 and later. The App Store app ID of the app that displays the ad. The `source-app-id` value matches [`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier`](skstoreproductparameteradnetworksourceappstoreidentifier.md) or [`sourceAppStoreItemIdentifier`](skadimpression/sourceappstoreitemidentifier.md).

Note: The `source-app-id` only appears in the postback if providing the parameter meets Apple’s privacy threshold.

- **`source-domain`**: Version 4 and later, for web ads only. For more information, see [`SKAdNetwork for Web Ads`](https://developer.apple.com/documentation/skadnetworkforwebads).
- **`conversion-value`**: Version 2 and later. An unsigned 6-bit value that the installed app sets by calling a method to update the conversion value, such as [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md). The `conversion-value` only appears in the postback if the installed app provides it, and if providing the parameter meets Apple’s privacy threshold.

Note: The signature doesn’t include the `conversion-value`. Postbacks may contain either `conversion-value` or `coarse-conversion-value`, not both.

- **`coarse-conversion-value`**: Version 4 and later. Possible values are the strings `"low"`, `"medium"`, and `"high"`. The installed app sets this value by calling a method to update conversion values, such as [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md).

Note: The signature doesn’t include the `coarse-conversion-value`. Postbacks may contain either `conversion-value` or `coarse-conversion-value`, not both.

- **`did-win`**: Version 3 and later. A Boolean value that’s `true` if the ad network wins the attribution, and `false` if the postback represents a qualifying ad impression that doesn’t win the attribution.
- **`fidelity-type`**: Version 2.2 and later. A value of `0` indicates a view-through ad presentation; a value of `1` indicates a StoreKit-rendered ad or an SKAdNetwork-attributed web ad.
- **`postback-sequence-index`**: Version 4 and later. The possible integer values of `0`, `1`, and `2` signify the order of postbacks that result from the three conversion windows. For more information, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).
- **`redownload`**: Version 2 and later. A Boolean value of `true` indicates that a device with the customer’s Apple Account previously installed the app.
- **`transaction-id`**: Version 1 and later. A unique value for this validation; use it to deduplicate install-validation postbacks.
- **`country-code`**: An ISO 3166-2 two-letter country identifier. It comes from the location of the signed-in account at the time of the app install.

To ensure crowd anonymity, Apple assigns a postback data tier to app downloads. The postback data tier determines whether certain parameters appear in the postback, as well as the number of digits in the hierarchical source identifier. The following postback parameters are subject to the postback data tier:

- `source-identifier` (affects the number of digits the postback returns)
- `coarse-conversion-value`
- `conversion-value`
- `source-app-id`
- `source-domain`
- `country-code`

For more information about receiving postbacks, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

- [Verifying an install-validation postback](verifying-an-install-validation-postback.md)
  Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/identifying-the-parameters-in-install-validation-postbacks)*