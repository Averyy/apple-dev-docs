# ReviewSubmissionCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data wrapper for a review submission create request, containing the resource type and app relationship.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object ReviewSubmissionCreateRequest.Data
```

## Topics

### Objects
- [object ReviewSubmissionCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a review submission create request resource.
- [object ReviewSubmissionCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (ReviewSubmissionCreateRequest.Data.Attributes)
- `relationships` (ReviewSubmissionCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `reviewSubmissions`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmissioncreaterequest/data-data.dictionary)*