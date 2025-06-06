# Identifying the parameters in install-validation postbacks

**Framework**: StoreKit

Learn about the postback parameters in all SKAdNetwork versions.

#### Overview

The following list describes all the possible parameters you may get in a postback, and their version availability. To verify that Apple signed the postback, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

Note: The `source-app-id` only appears in the postback if providing the parameter meets Apple’s privacy threshold.

Note: The signature doesn’t include the `conversion-value`. Postbacks may contain either `conversion-value` or `coarse-conversion-value`, not both.

Note: The signature doesn’t include the `coarse-conversion-value`. Postbacks may contain either `conversion-value` or `coarse-conversion-value`, not both.

To ensure crowd anonymity, Apple assigns a postback data tier to app downloads. The postback data tier determines whether certain parameters appear in the postback, as well as the number of digits in the hierarchical source identifer. The following postback parameters are subject to the postback data tier:

- `source-identifier` (affects the number of digits the postback returns)
- `coarse-conversion-value`
- `conversion-value`
- `source-app-id`
- `source-domain`

For more information about receiving postbacks, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

- [Verifying an install-validation postback](verifying-an-install-validation-postback.md)
  Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/identifying-the-parameters-in-install-validation-postbacks)*