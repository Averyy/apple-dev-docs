# Managing merchant IDs and Payment Processing certificates

**Framework**: Appstoreconnectapi

Create and update certificates so your app uses Apple Pay and Wallet.

#### Overview

Managing your merchant Identifier (ID) and Payment Processing certificates keeps the Apple Pay service active in your app. To set up your Apple developer account and Xcode to implement Apple Pay in your apps, complete three steps:

- Create a merchant ID.
- Create a Payment Processing certificate. To learn more about certificates for Apple Pay and Wallet, see [`Configure Apple Pay`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay/).
- Enable Apple Pay in Xcode. To learn more see, [`Setting up Apple Pay`](https://developer.apple.comhttps://developer.apple.com/documentation/passkit/setting-up-apple-pay) Once you set up Apple Pay in your apps, you then can replace Payment Processing certificates as they near their expiration date — 25 months after you create them. To learn more, see [`Maintaining Your Environment`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/maintaining_your_environment#overview).

##### Create a Merchant Id

A merchant ID uniquely identifies you to Apple Pay as a merchant who is able to accept payments. A merchant ID never expires, and you can use the same one for multiple apps.

To create a merchant ID, use [`Create a merchant ID`](post-v1-merchantids.md).

Here’s an example payload:

```json
"data": {
        "type": "merchantIds",
        "attributes": {
            "identifier": "com.myapp.merchant1",
            "name": "MyMerchantName"
        }
    }
}
```

> **Note**: The value for `identifier` is a unique identifier for your merchant. The value for `name` is a descriptive name for the merchant.

##### Create Payment Processing Certificate

To create a certificate to use with Apple Pay, use [`Create a Certificate`](post-v1-certificates.md).

Here’s an example payload:

```json
{
  "data": {
    "type": "certificates",
    "attributes": {
        "certificateType": "APPLE_PAY",
        "csrContent" : "<PEM-CSR-Content>"
    },
    "relationships": {
      "merchantId": {
        "data": {
          "type": "merchantIds",
          "id": "1234567890"
        }
      }
    }
  }
}
```

> **Note**: The `id` field in the example payload is a 10-character string that the prior request returns. The `csrContent` is your certificate-signing request.

##### Rotate a Payment Processing Certificate

Use one of three options to replace a payment-processing certificate nearing its 25-month expiration date. Each option takes into account that you can have more than one payment processing certificate, but only one can be `activated` for use at any time:

> **Note**: The “Create and activate” option also deactivates the expiring certificate by automatically setting the `activated` key to `FALSE`.

## See Also

- [List merchant IDs](get-v1-merchantids.md)
  List all merchant Ids for your team.
- [Read details for a merchant ID](get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificates for a merchant ID](get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [Modify merchant IDs](patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a merchant ID](post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant ID](delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/managing-payment-processing-certificates)*