# InAppPurchaseSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A submission of an in-app purchase to App Store review, triggering the review process for that item.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseSubmission
```

## Topics

### Objects
- [object InAppPurchaseSubmission.Relationships](inapppurchasesubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchaseSubmission.Relationships)
- `type` (string) *(required)*

## See Also

- [object InAppPurchaseSubmissionCreateRequest](inapppurchasesubmissioncreaterequest.md)
  The request body you use to create an in-app purchase submission.
- [object InAppPurchaseSubmissionResponse](inapppurchasesubmissionresponse.md)
  A response confirming the submission of an in-app purchase for App Store review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasesubmission)*