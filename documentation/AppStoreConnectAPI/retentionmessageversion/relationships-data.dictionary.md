# RetentionMessageVersion.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships you include in the request and those on which you can operate.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersion.Relationships
```

## Topics

### Objects
- [object RetentionMessageVersion.Relationships.RetentionMessage](./relationships-data.dictionary/retentionmessage-data.dictionary.md)
  The data and links that describe the relationship between the resources.
- [object RetentionMessageVersion.Relationships.Localizations](./relationships-data.dictionary/localizations-data.dictionary.md)
  The data and links that describe the relationship between the resources.
- [object RetentionMessageVersion.Relationships.Placement](./relationships-data.dictionary/placement-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `retentionMessage` (RetentionMessageVersion.Relationships.RetentionMessage): The retention message that the version belongs to.
- `localizations` (RetentionMessageVersion.Relationships.Localizations): The localized header and body text of the version.
- `placement` (RetentionMessageVersion.Relationships.Placement): The asset library image placement that appears with the retention message.

## See Also

### Objects
- [object RetentionMessageVersion.Attributes](./attributes-data.dictionary.md)
  Attributes that describe a retention message version resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversion/relationships-data.dictionary)*