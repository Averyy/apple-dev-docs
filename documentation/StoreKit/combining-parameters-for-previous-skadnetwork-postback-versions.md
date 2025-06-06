# Combining parameters for previous SKAdNetwork postback versions

**Framework**: StoreKit

Recreate the byte array for versions 2.2 or earlier.

#### Overview

Combine postback parameters to recreate a byte array that you use to verify Apple’s signature. To recreate the byte array, create a UTF-8 string by combining the parameter values in an exact order, with an invisible separator (`‘\u2063’`) between them. You must combine the parameters in the exact orders as show in the examples. For more information about the parameters and verifying the signature, and an example using newer versions, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

##### Combine Postback Parameters for Version 22

The following JSON shows an example of a version 2.2 install-validation postback that contains all possible parameters and a valid signature:

```javascript
{
  "version" : "2.2",
  "ad-network-id" : "com.example",
  "campaign-id" : 42,
  "transaction-id" : "6aafb7a5-0170-41b5-bbe4-fe71dedf1e28",
  "app-id" : 525463029,
  "attribution-signature" : "MEYCIQDTuQ1Z4Tpy9D3aEKbxLl5J5iKiTumcqZikuY/AOD2U7QIhAJAaiAv89AoquHXJffcieEQXdWHpcV8ZgbKN0EwV9/sY",
  "redownload": true,
  "source-app-id": 1234567891,
  "fidelity-type": 1,
  "conversion-value": 20
}  
```

To verify the signature, combine version 2.2 postback parameters in this order:

- `version`
- `ad-network-id`
- `campaign-id`
- `app-id`
- `transaction-id`
- `redownload` Note: use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.
- `source-app-id`
- `fidelity-type`

Include `source-app-id` only if you received it in the postback. Note that the signature never includes a conversion value, even if it’s present in the postback.

The following is an example of the UTF-8 string for a postback with `source-app-id` present in the postback:

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + source-app-id
+ '\u2063' + fidelity-type
 
```

The following is an example of the UTF-8 string for a postback without `source-app-id`:

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + fidelity-type

```

##### Combine Postback Parameters for Versions 2 and 21

Version 2 and 2.1 postbacks contain the following parameters. Combine their values in this order:

- `version`
- `ad-network-id`
- `campaign-id`
- `app-id`
- `transaction-id`
- `redownload` Note: use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter.
- `source-app-id`

Include `source-app-id` only if you receive it in the postback. Note that the signature never includes a conversion value, even if it’s present in the postback.

The following is an example of the UTF-8 string for a postback with `source-app-id` present in the postback:

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + source-app-id
 
```

The following is an example of the UTF-8 string for a postback without `source-app-id`:

```swift
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload

```

##### Combine Postback Parameters for Version 1

Version 1 postbacks contain the following parameters. Combine their values in this order:

- `ad-network-id`
- `campaign-id`
- `app-id`
- `transaction-id`

The following is an example of the UTF-8 string for a version 1.0 postback:

```javascript
ad-network-id + '\u2063' + campaign-id + '\u2063' + app-id + '\u2063' + transaction-id 
```

## See Also

- [Combining parameters for SKAdNetwork 3 postbacks](combining-parameters-for-skadnetwork-3-postbacks.md)
  Recreate the byte array for version 3 postbacks that win and don’t win attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/combining-parameters-for-previous-skadnetwork-postback-versions)*