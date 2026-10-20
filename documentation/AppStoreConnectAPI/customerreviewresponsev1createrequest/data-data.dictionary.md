# CustomerReviewResponseV1CreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body for creating a response to a customer review.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object CustomerReviewResponseV1CreateRequest.Data
```

## Topics

### Objects
- [object CustomerReviewResponseV1CreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes of the customer review response, including its text content.
- [object CustomerReviewResponseV1CreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (CustomerReviewResponseV1CreateRequest.Data.Attributes) *(required)*: The attributes of the customer review response, including its text content.
- `relationships` (CustomerReviewResponseV1CreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `customerReviewResponses`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewresponsev1createrequest/data-data.dictionary)*