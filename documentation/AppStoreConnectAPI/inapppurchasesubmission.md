# InAppPurchaseSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A submission of an In-App Purchase to App Store review, triggering the review process for that item.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use the review submissions workflow instead.

## Declaration

```
object InAppPurchaseSubmission
```

## Topics

### Objects
- [object InAppPurchaseSubmission.Relationships](./inapppurchasesubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchaseSubmission.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `inAppPurchaseSubmissions`

## See Also

### Objects
- [object InAppPurchaseSubmissionCreateRequest](./inapppurchasesubmissioncreaterequest.md)
  The request body you use to create an In-App Purchase submission.
- [object InAppPurchaseSubmissionResponse](./inapppurchasesubmissionresponse.md)
  A response confirming the submission of an In-App Purchase for App Store review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasesubmission)*