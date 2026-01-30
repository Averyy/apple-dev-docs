# AdServices

**Framework**: AdServices  
**Kind**: module

Attribute app-download campaigns that originate from the App Store on iOS devices.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Mentions

- [Changelog](changelog.md)

#### Overview

The Apple Ads Attribution API is a solution that combines the `AdServices` framework and a RESTful API for server-side communication with Apple’s attribution server. The API retrieves Apple Ads attribution data from Apple Ads campaigns. You can measure attribution data using specific Apple Ads campaign metadata against the performance of Apple Ads campaigns.

The following diagram illustrates using the AdServices framework in combination with a RESTful endpoint to retrieve attribution data:

![A diagram showing the sequence of interaction between the AdServices framework and RESTful API.](https://docs-assets.developer.apple.com/published/f0cd7bd0fb49333e7481ce470651a1cf/ad_services-1%402x.png)

- In step 1, request a token from the `AdServices` framework.
- In step 2, the `AdServices` framework generates a token.
- In step 3, use the token in a RESTful API request to retrieve an attribution record from Apple’s attribution server. For more detail, see [`attributionToken()`](aaattribution/attributiontoken().md).
- In step 4, the attribution record that returns has key-value pairs that correspond to your campaigns in the Apple Ads Campaign Management API. For more detail, see [`Attribution payload descriptions`](aaattribution/attributiontoken()#Attribution-payload-descriptions.md).

## Topics

### Essentials
- [Changelog](changelog.md)
  A log of Ad Services framework updates.
### Tokens
- [class AAAttribution](aaattribution.md)
  The parent class that the framework uses to request a token.
### Errors
- [struct AAAttributionError](aaattributionerror.md)
  The error code that the parent class issues.
- [let AAAttributionErrorDomain: String](aaattributionerrordomain.md)
  The framework attribution error domain.
- [AAAttributionError.Code](aaattributionerror/code.md)
  The error code that the parent class issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdServices)*