# TN3122: Receipt validation with the App Store fails with a non-zero error code

**Framework**: Technotes

Identify common configurations that cause unsuccessful receipt validation with the App Store.

#### Overview

Receipt validation with the App Store requires that you send a JSON object with the `receipt-data` and `password` keys, and optionally the `exclude-old-transactions` key as detailed in [`requestBody`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/requestbody). The App Store responds with a value of `0` if validation was successful, and a [`status code`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/status) if validation failed. This document lists reasons for unsuccessful validations.

#### Encoding of the Receipt Data Failed

Validating the receipt with the App Store requires encoding the receipt data using Base64 in your app before sending it to your server. Use [`Data.base64EncodedString(options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/data/2142853-base64encodedstring/) as detailed in [`Fetch the Receipt Data`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase/validating_receipts_with_the_app_store) or a Base64 algorithm of your choosing to encode the receipt data. if you use a different Base64 algorithm, confirm that it successfully covers and encodes all possible characters in a receipt.

#### Shared Secret Is Invalid

In App Store Connect, you can generate or regenerate a primary shared secret for all of your apps, or an app-specific shared secret for each of your apps. When you regenerate the primary shared secret, you invalidate the previous shared secret for all of your apps that use it. Confirm that the `password` key is set to the latest value of the primary shared secret for all of your apps that use it. See [`Generate a shared secret`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devf341c0f01) for details.

When you generate an app-specific shared secret for an app, that app can no longer use the primary shared secret. Confirm that `password` is set to the
latest value of the app-specific shared secret for this app. The app-specific shared secret becomes invalid for the app when you regenerate it.

#### Object Posted to the App Store Is Invalid

On your server, create and format an object as JSON. This JSON object is a dictionary that contains the `receipt-data` and `password` keys. Each key pair in the dictionary is separated by a comma.

```json
{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
}
```

For receipts that contain auto-renewable subscriptions, optionally add `exclude-old-transactions` to the JSON object. The [`latest_receipt_info`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/responsebody/latest_receipt_info) key contains the most recent entry for any subscriptions when `exclude-old-transactions` is set to `true` and all renewal entries, otherwise.

```json
{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
    "exclude-old-transactions": true
}
```

If `exclude-old-transactions` is absent in the JSON object, then the default value is `false`.

> ❗ **Important**: On your server, be sure to send your JSON object as the payload of an HTTP POST request for receipt validation with the App Store.

#### Validation Request Was Posted to the Incorrect Url

Use the sandbox URL to verify receipts when testing in the sandbox and while your app is in review:

```None
https://sandbox.itunes.apple.com/verifyReceipt
```

Use the production URL to verify receipts when your app is live in the App Store:

```None
https://buy.itunes.apple.com/verifyReceipt
```

First, verify your receipt with the production URL. If you receive a `21007` status code, as outlined in [`verifyReceipt`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/verifyreceipt), verify with the sandbox URL instead.

> **Note**: TestFlight uses the sandbox environment for in-app purchases. See [`Testing at All Stages of Development with Xcode and Sandbox`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/in-app_purchase/testing_at_all_stages_of_development_with_xcode_and_sandbox) for details.

#### Validate the Receipt Locally

Consider validating your receipt locally with the App Store to ensure your implementation works as designed. Use the `curl` command to test your JSON object.

To validate your receipt in the sandbox environment, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret"
 }' 
 https://sandbox.itunes.apple.com/verifyReceipt
```

To validate your receipt in the production environment, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret"
 }' 
 https://buy.itunes.apple.com/verifyReceipt
```

To validate your receipt in the production environment and limit the content of the `latest_receipt_info` key to only the most recent entry, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
    "exclude-old-transactions": true
 }' 
 https://buy.itunes.apple.com/verifyReceipt
```

#### Revision History

- **2022-05-24** Made minor editorial changes.
- **2022-04-26** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3122-receipt-validation-with-the-app-store-fails-with-a-non-zero-error-code)*