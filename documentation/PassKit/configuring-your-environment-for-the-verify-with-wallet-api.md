# Configuring your environment for the Verify with Wallet API

**Framework**: PassKit (Apple Pay and Wallet)

Set up your environment to use Verify with Wallet.

#### Overview

Verify with Wallet allows you to verify a person’s information using their digital ID stored in Apple Wallet. Verify with Wallet streamlines the verification experience in apps that use age or identity verification by allowing people to share information from their digital ID.

To request a digital ID stored in Apple Wallet, you use the [`PKIdentityNationalIDCardDescriptor`](pkidentitynationalidcarddescriptor.md). You need the `in-app-identity-presentment` entitlement to use this API, and you can [`submit your request here`](https://developer.apple.comhttps://developer.apple.com/contact/request/verify-with-wallet/). For more information on the Verify with Wallet API and entitlement requirements, see [`Get started with the Verify with Wallet API`](https://developer.apple.comhttps://developer.apple.com/wallet/get-started-with-verify-with-wallet/).

#### Set Up Your Developer Account

After you add the `in-app-identity-presentment` entitlement, you’ll set up your developer account. Complete the following steps in the Certificates, Identifiers, & Profiles section of the Apple Developer website:

1. Create a merchant ID. If you already have a merchant ID you use for Apple Pay, you can reuse it here.
2. Create an  for your merchant ID. This certificate shows up in the  tab on the  page. Note that your server uses the private key of the encryption certificate to decrypt the encrypted data returned from the API.
3. Add the `In App Identity Presentment` capability to your App ID. This capability appears in the  tab of the  page.
4. Add the ‘In App Identity Presentment Merchant IDs’ capability to your App ID and select the associated Merchant IDs.
5. Generate a new provisioning profile with these changes.

#### Configure Your Apps Entitlement File

Choose the `document-type` you want to add the entitlement to from the entitlement request you submitted. For more information, see [`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

Filter the list of entitlements to just the ones you requested through the entitlement request. The following example shows what a entitlement with the `us-drivers-license` doc-type request might look like:

```json

"com.apple.developer.in-app-identity-presentment": {
    "document-types": [
        "us-drivers-license"
    ],
    "elements": [
        "given-name",
        "family-name",
        "portrait",
        "address",
        "issuing-authority",
        "document-expiration-date",
        "document-number",
        "driving-privileges",
        "age",
        "date-of-birth"
    ]
},

"com.apple.developer.in-app-identity-presentment.merchant-identifiers": [
    “your-merchant-id-goes-here”
]

```

You must add the `com.apple.developer.in-app-identity-presentment.merchant-identifiers` entitlement even if you’re using the same merchant ID for Apple Pay. Apple Pay’s `com.apple.developer.in-app-payments` entitlement isn’t recognized for identity verification.

Once you’ve set up your developer environment, you can use the [`PKIdentityNationalIDCardDescriptor`](pkidentitynationalidcarddescriptor.md) API to request a digital ID stored in Apple Wallet.

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
- [class PKIdentityPhotoIDDescriptor](pkidentityphotoiddescriptor.md)
  An object you use to request information from a user’s photo ID or equivalent document.
- [class PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md)
  An object you use to request information from multiple identity documents.
- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md)
  The object for specifying the metadata necessary to provision identity documents.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/configuring-your-environment-for-the-verify-with-wallet-api)*