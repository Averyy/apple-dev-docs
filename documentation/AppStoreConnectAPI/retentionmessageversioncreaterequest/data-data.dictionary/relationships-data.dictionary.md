# RetentionMessageVersionCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersionCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object RetentionMessageVersionCreateRequest.Data.Relationships.RetentionMessage](./relationships-data.dictionary/retentionmessage-data.dictionary.md)
  The relationships to other resources that you can set with this request.
- [object RetentionMessageVersionCreateRequest.Data.Relationships.Placement](./relationships-data.dictionary/placement-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `retentionMessage` (RetentionMessageVersionCreateRequest.Data.Relationships.RetentionMessage) *(required)*: The retention message to create a version for.
- `placement` (RetentionMessageVersionCreateRequest.Data.Relationships.Placement): The asset library image placement to show with the retention message. Omit the placement for a text-only message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversioncreaterequest/data-data.dictionary/relationships-data.dictionary)*