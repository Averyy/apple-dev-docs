# InAppPurchaseSubmissionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response confirming the submission of an in-app purchase for App Store review.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseSubmissionResponse
```

## Properties

- `data` (InAppPurchaseSubmission) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (DocumentLinks) *(required)*

## See Also

- [object InAppPurchaseSubmissionCreateRequest](inapppurchasesubmissioncreaterequest.md)
  The request body you use to create an in-app purchase submission.
- [object InAppPurchaseSubmission](inapppurchasesubmission.md)
  A submission of an in-app purchase to App Store review, triggering the review process for that item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasesubmissionresponse)*