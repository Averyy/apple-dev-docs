# Registering with Apple Pay and Applying to Use the API

**Framework**: Apple Pay Web Merchant Registration API

Register a commerce partner with Apple Pay and apply to use the web service.

#### Overview

An e-commerce platform that’s enrolled in the Apple Developer program as an organization can apply to use the Apple Pay Web Merchant Registration API by completing the following steps:

1. Create your unique Apple Pay merchant ID.
2. Sign in the Apple Developer and fill out the [`submission form `](https://developer.apple.comhttps://developer.apple.com/contact/request/apple-pay-web-merchant-registration-api)to request access to the API.
3. Set up your Payment Processing Certificate and Merchant Identity Certificate.

Once Apple grants you access to the API, you receive one or more domain-verification files. You must host a domain-verification file on a merchant’s domain before registering the merchant. For more information about domain verification, see [`Preparing Merchant Domains for Verification`](preparing-merchant-domains-for-verification.md).

##### Create Your Apple Pay Merchant Id

To apply to use the Apple Pay Web Merchant Registration API, you’ll need an Apple Pay merchant ID. This unique ID identifies you to Apple Pay as an entity that’s able to accept payments. Create your merchant ID and register it with Apple in your developer account. Merchant IDs never expire.

To create your merchant ID, log in to your Apple developer account with the Account Holder or Admin role. Then:

1. In [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/certificates/list), select Identifiers from the sidebar.
2. Select App IDs in the upper-right corner, and then select Merchant IDs.
3. Select the Add button (+).
4. Enter the merchant description and identifier name, then click Continue.
5. Review the settings, then click Register.

The identifier name you entered is your merchant ID. If you have multiple environments, such as production and sandbox, you may choose to create additional merchant IDs for other environments.

Once you have at least one merchant ID, you’re ready to log in to your Apple developer account and fill out the [`submission form `](https://developer.apple.comhttps://developer.apple.com/contact/request/apple-pay-web-merchant-registration-api) to request access to the API.

##### Create Payment Processing and Merchant Identity Certificates

To complete your Apple Pay set up, create the two certificates associated with your merchant ID:

- A payment processing certificate that Apple Pay servers use to encrypt payment data
- A merchant identity certificate that you use to authenticate communication with Apple Pay servers

To create the certificates, log in to your Apple developer account using the Account Holder or Admin roles. For the payment processing certificate, see [`Create a payment processing certificate`](https://developer.apple.comhttps://help.apple.com/developer-account/#/devb2e62b839?sub=devf31990e3f). For the merchant identity certificate, see [`Create a merchant identity certificate`](https://developer.apple.comhttps://help.apple.com/developer-account/#/dev1731126fb).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registering-with-apple-pay-and-applying-to-use-the-api)*