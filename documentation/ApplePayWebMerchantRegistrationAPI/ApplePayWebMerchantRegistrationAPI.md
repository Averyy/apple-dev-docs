# Apple Pay Web Merchant Registration API

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: module

Manage merchant registration through your web platform.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

#### Overview

The Apple Pay Web Merchant Registration API is a REST API that enables platform integrators such as payment-service providers and e-commerce platforms to register web merchants who want to offer Apple Pay on the web.

As a platform integrator, you manage Apple Pay configuration on the merchants’ behalf when you call [`Register Merchant`](register-merchant.md). Merchants aren’t required to set up an Apple Developer account or configure their own keys and certificates — you set up a shared set of keys and certificates for your entire merchant portfolio. Register merchants with their own website domains, or with web pages hosted by your platform.

> **Note**:  This API is available in production and in sandbox environments. To use this API in the sandbox environment, call the endpoints using the domain `apple-pay-gateway-cert.apple.com`.  For example, the sandbox endpoint for [`Register Merchant`](register-merchant.md) is: `POST https://apple-pay-gateway-cert.apple.com/paymentservices/registerMerchant`.

##### Api Requirements for Use

To use the Apple Pay Web Merchant Registration API,  you must meet the following requirements:

- Your organization must be enrolled in the Apple Developer program. For more information about enrollment, see the “Enrolling as an Organization” section in [`What You Need To Enroll`](https://developer.apple.comhttps://developer.apple.com/programs/enroll/).
- You must apply for access to the API. For more information about applying, see [`Registering with Apple Pay and Applying to Use the API`](registering-with-apple-pay-and-applying-to-use-the-api.md).
- Your server must call the API using mutual authentication with Transport Layer Security (TLS) 1.2 or later, and one of the supported cipher suites. For a list of supported cipher suites, see [`Setting Up Your Server`](https://developer.apple.com/documentation/ApplePayontheWeb/setting-up-your-server).

## Topics

### Essentials
- [Registering with Apple Pay and Applying to Use the API](registering-with-apple-pay-and-applying-to-use-the-api.md)
  Register a commerce partner with Apple Pay and apply to use the web service.
### Web Merchant Registration
- [Preparing Merchant Domains for Verification](preparing-merchant-domains-for-verification.md)
  Host a domain verification file on each domain before requesting registration.
- [Register Merchant](register-merchant.md)
  Register a merchant and its corresponding set of fully qualified domains.
- [object RegisterMerchantRequest](registermerchantrequest.md)
  The request body you use to register merchants.
### Web Merchant Unregistration
- [Unregister Merchant](unregister-merchant.md)
  Unregister one or more domains associated with a previously registered merchant.
- [object UnregisterMerchantRequest](unregistermerchantrequest.md)
  The request body you use to unregister one or more merchant domains.
### Web Merchant Details
- [Get Merchant Details](get-merchant.md)
  Retrieve information about a registered merchant’s current state by using the merchant’s internal merchant identifier.
- [object MerchantDetails](merchantdetails.md)
  Detailed information for a single registered merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI)*