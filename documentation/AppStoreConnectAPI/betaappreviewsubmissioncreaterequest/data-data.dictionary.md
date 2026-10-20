# BetaAppReviewSubmissionCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaAppReviewSubmissionCreateRequest.Data
```

## Topics

### Objects
- [object BetaAppReviewSubmissionCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `relationships` (BetaAppReviewSubmissionCreateRequest.Data.Relationships) *(required)*: The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaAppReviewSubmissions`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewsubmissioncreaterequest/data-data.dictionary)*