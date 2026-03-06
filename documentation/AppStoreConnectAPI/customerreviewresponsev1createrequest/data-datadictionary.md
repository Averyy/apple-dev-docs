# CustomerReviewResponseV1CreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body for creating a response to a customer review.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReviewResponseV1CreateRequest.Data
```

## Topics

### Objects
- [object CustomerReviewResponseV1CreateRequest.Data.Attributes](customerreviewresponsev1createrequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes of the customer review response, including its text content.
- [object CustomerReviewResponseV1CreateRequest.Data.Relationships](customerreviewresponsev1createrequest/data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (CustomerReviewResponseV1CreateRequest.Data.Attributes) *(required)*: The attributes of the customer review response, including its text content.
- `relationships` (CustomerReviewResponseV1CreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewresponsev1createrequest/data-data.dictionary)*