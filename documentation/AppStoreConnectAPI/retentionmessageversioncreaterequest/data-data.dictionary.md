# RetentionMessageVersionCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersionCreateRequest.Data
```

## Topics

### Objects
- [object RetentionMessageVersionCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessageVersions`
- `relationships` (RetentionMessageVersionCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversioncreaterequest/data-data.dictionary)*