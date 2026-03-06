# BetaAppReviewDetail.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a Beta App Review Details resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewDetail.Attributes
```

## Properties

- `contactEmail` (string): Email address of contact in case communication is needed with the beta app review.
- `contactFirstName` (string): First name of contact in case communication is needed with the beta app review.
- `contactLastName` (string): Last name of contact in case communication is needed with the beta app review.
- `contactPhone` (string): Phone number of contact in case communication is needed with the beta app review.
- `demoAccountName` (string): The user name to sign in to your app to review its features.
- `demoAccountPassword` (string): The password to sign in to your app to review its features.
- `demoAccountRequired` (boolean): A Boolean value that indicates if sign-in information is required to review all the features of your app. If users sign in using social media, provide information for an account for review. Credentials must be valid and active for duration of review.
- `notes` (string): Additional information about your app that can help during the review process. Do not include demo account details. Review notes have a maximum of 4,000 characters.

## See Also

- [Beta App Review Detail](beta-app-review-detail.md)
  Information about your app required for beta app review.
- [object BetaAppReviewDetail.Relationships](betaappreviewdetail/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewdetail/attributes-data.dictionary)*