# Combining parameters for SKAdNetwork 3 postbacks

**Framework**: StoreKit

Recreate the byte array for version 3 postbacks that win and don’t win attribution.

#### Overview

Check your postback’s version, and use the version-specific instructions to combine the parameters to validate the postback. The order of the parameters depends on the version of the postback you receive.

To verify the signature, combine the postback parameter values in this order for a version 3 postback:

- `version`
- `ad-network-id`
- `campaign-id`
- `app-id`
- `transaction-id`
- `redownload` (Use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.)
- `source-app-id`
- `fidelity-type`
- `did-win`

Include `source-app-id` only if you receive it in the postback. Note that the signature doesn’t include a conversion value, even if it’s present in the postback. Postbacks that win the attribution have a `did-win` value of `true`. Postbacks that don’t win the attribution have a `did-win` value of `false`, and don’t include `source-app-id`.

The following example of the UTF-8 string includes `source-app-id:`

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + did-win
 
```

The following example of the UTF-8 string doesn’t include `source-app-id:`

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + fidelity-type + '\u2063' + did-win

```

##### Receive the Winning Postback with Attribution

The following JSON example shows a version 3 install-validation postback the device sends to an ad network that wins the attribution. This example contains all possible parameters and a valid signature:

```javascript
{ 
  "version": "3.0", 
  "ad-network-id": "example123.skadnetwork", 
  "campaign-id": 42, 
  "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e28", 
  "app-id": 525463029, 
  "attribution-signature": "MEYCIQD5eq3AUlamORiGovqFiHWI4RZT/PrM3VEiXUrsC+M51wIhAPMANZA9c07raZJ64gVaXhB9+9yZj/X6DcNxONdccQij", 
  "redownload": true, 
  "source-app-id": 1234567891, 
  "fidelity-type": 1, 
  "conversion-value": 20,
  "did-win": true
}
```

##### Receive a Nonwinning Postback Without Attribution

In iOS 14.6 and later, ad networks that sign ads with version 3 may receive a postback for their qualifying ad impression that don’t win the attribution. Such postbacks have a `did-win` value of `false`, and don’t include `source-app-id` or `conversion-value`.

The following example shows a version 3 postback for an ad that doesn’t win the attribution. This example contains all the parameters the system includes in a nonwinning postback:

```javascript
{ 
  "version": "3.0",
  "ad-network-id": "example123.skadnetwork",
  "campaign-id": 42,
  "transaction-id": "f9ac267a-a889-44ce-b5f7-0166d11461f0",
  "app-id": 525463029,
  "attribution-signature": "MEUCIQDDetUtkyc/MiQvVJ5I6HIO1E7l598572Wljot2Onzd4wIgVJLzVcyAV+TXksGNoa0DTMXEPgNPeHCmD4fw1ABXX0g=",
  "redownload": true,
  "fidelity-type": 1,
  "did-win": false
}
```

Up to five ad networks may receive a nonwinning postback. A single ad network can receive at most one postback per advertised app, per conversion. For example, if the device registers three qualifying ad impressions from your ad network, you receive only one postback.

If your ad network wins the attribution, you only receive the winning postback, even if the device registers other qualifying impressions for your ad.

For more information about ad impressions qualifying for attribution, and receiving winning or nonwinning postbacks, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

## See Also

- [Combining parameters for previous SKAdNetwork postback versions](combining-parameters-for-previous-skadnetwork-postback-versions.md)
  Recreate the byte array for versions 2.2 or earlier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/combining-parameters-for-skadnetwork-3-postbacks)*